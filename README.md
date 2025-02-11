# DNS Lookup API

<img src="/assets/DnsLookup.png" alt="DNS Lookup API" width="500">

A lightweight DNS lookup API built with Flask and dnspython, providing DNS record querying capabilities. Supports multiple record types with rate-limited requests.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FTheBiemGamer%2FDNSLookupAPI)

### Features:
- Web interface with domain input and record type selector
- Dark/light theme toggle
- API endpoint at `/lookup?domain=<domain>&type=<record_type>`
- Rate limiting (enabled by default)
- Multiple DNS record type support (A, AAAA, MX, TXT, etc.)

---

## Setup Instructions

### Prerequisites
- [Docker](https://www.docker.com/) (for containerized deployment)
- [Python 3.9+](https://www.python.org/) (for local development)

### 1. Clone the repository
```bash
git clone https://github.com/TheBiemGamer/DNSLookupAPI.git
cd DNSLookupAPI
```

### 2. Docker Setup (Recommended)
```bash
docker build -t dns-lookup .
docker run -p 5000:5000 dns-lookup
```
Visit `http://localhost:5000`

### 3. Local Installation
```bash
pip install -r requirements.txt
```

Run with Flask (development):
```bash
cd dnslookupapi
flask run 
```

Or with Waitress (production-ready):
```bash
waitress-serve dnslookupapi.app:app
```

---

## API Endpoint

**GET** `/lookup`

**Parameters**:
- `domain`: Domain name (required, e.g., `example.com`)
- `type`: Record type (optional, default: `A`)

**Example Request**:
```http
GET /lookup?domain=example.com&type=MX
```

**Success Response**:
```json
{
  "domain": "example.com",
  "record_type": "MX",
  "records": [
    "10 mail.example.com"
  ]
}
```

**Error Responses**:
```json
{
  "error": "No MX record found for example.com"
}
```

```json
{
  "error": "Domain nonexistent.com does not exist."
}
```

---

## Rate Limiting

Configured via `.env` file (copy from `.env.example`):
- Enabled by default
- Limits: 5/minute, 100/hour, 500/day
- Per-endpoint limit: 1/second

Disable by setting:
```env
ENABLE_RATE_LIMIT=False
```

---

## Supported Record Types
- A (IPv4 Address)
- AAAA (IPv6 Address)
- MX (Mail Exchange)
- TXT (Text Record)
- CNAME (Canonical Name)
- NS (Name Server)
- SOA (Start of Authority)

---

## Credits

Built using:
- [dnspython](https://www.dnspython.org/) - DNS toolkit for Python
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Flask-Limiter](https://flask-limiter.readthedocs.io/) - Rate limiting

---

## License

MIT License - See [LICENSE](LICENSE)

---

## Author

- [TheBiemGamer](https://github.com/TheBiemGamer)