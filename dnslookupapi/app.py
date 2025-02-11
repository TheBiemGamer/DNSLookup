from flask import Flask, jsonify, render_template, request
import dns.resolver
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ENABLE_RATE_LIMIT = os.getenv("ENABLE_RATE_LIMIT", "True").lower() == "true"

if ENABLE_RATE_LIMIT:
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["5 per minute", "100 per hour", "500 per day"]
    )

    @limiter.request_filter
    def exempt_requests():
        """Allow exemptions (e.g., internal requests if needed)"""
        return False

    @app.errorhandler(429)
    def ratelimit_exceeded(e):
        return jsonify({
            "error": "Rate limit exceeded",
            "message": "Too many requests. Please slow down."
        }), 429
else:
    limiter = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/lookup', methods=['GET'])
@limiter.limit("1 per second") if ENABLE_RATE_LIMIT else None
def lookup():
    domain = request.args.get('domain')
    record_type = request.args.get('type', 'A').upper()

    if not domain:
        return jsonify({"error": "The 'domain' parameter is required."}), 400
    
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["8.8.8.8", "8.8.4.4"]

    try:
        answers = resolver.resolve(domain, record_type)
        records = [rdata.to_text() for rdata in answers]

        return jsonify({
            "domain": domain,
            "record_type": record_type,
            "records": records
        })

    except dns.resolver.NoAnswer:
        return jsonify({"error": f"No {record_type} record found for {domain}."}), 404
    except dns.resolver.NXDOMAIN:
        return jsonify({"error": f"Domain {domain} does not exist."}), 404
    except dns.resolver.NoNameservers:
        return jsonify({"error": "No nameservers available to answer the query."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)