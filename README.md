# DNS Lookup API

<img src="/assets/DnsLookup.png" alt="DNS Lookup API" width="500">

A DNS lookup API built with Flask and dnspython. Supports multiple record types with rate-limited requests.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FTheBiemGamer%2FDNSLookupAPI)

---

## Features

- **Web Interface:** Enter a domain and select the DNS record type.
- **Dark/Light Theme Toggle:** Switch between dark and light modes.
- **API Endpoint:**  
  - `/lookup?domain=<domain>&type=<record_type>`
- **Rate Limiting:** Enabled by default.
- **Multiple DNS Record Types:** Supports A, AAAA, MX, TXT, CNAME, NS, SOA, etc.

---

## Table of Contents

- [Installation via Docker (Online)](#installation-via-docker-online)
- [Local Setup Instructions](#local-setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#1-clone-the-repository)
  - [Docker Setup (Build Locally)](#2-docker-setup-build-locally)
  - [Running Locally Without Docker](#3-running-locally-without-docker)
- [API Endpoint](#api-endpoint)
- [Rate Limiting](#rate-limiting)
- [Supported Record Types](#supported-record-types)
- [Credits](#credits)
- [License](#license)
- [Author](#author)

---

## Installation via Docker (Online)

Run the pre-built Docker image from GitHub's Container Registry (no cloning required):

```bash
docker run -p 5000:5000 ghcr.io/thebiemgamer/dnslookupapi:latest
```

Visit [http://localhost:5000](http://localhost:5000) to access the API.

---

## Local Setup Instructions

### Prerequisites

- [Docker](https://www.docker.com/) *(optional — for containerized deployment)*
- [Python 3.9+](https://www.python.org/) *(for local development)*

### 1. Clone the Repository

For local development, clone the repository:

```bash
git clone https://github.com/TheBiemGamer/DNSLookupAPI.git
cd DNSLookupAPI
```

### 2. Docker Setup (Build Locally)

To build and run your own Docker image:

```bash
docker build -t dns-lookup .
docker run -p 5000:5000 dns-lookup
```

Visit [http://localhost:5000](http://localhost:5000) after the container starts.

### 3. Running Locally Without Docker

To run the app directly on your machine:

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Application**

   - **Using Flask's Development Server:**

     ```bash
     cd dnslookupapi
     flask run
     ```

   - **Using Gunicorn for a Production-like Environment:**

     ```bash
     gunicorn -w 4 -b 0.0.0.0:5000 dnslookupapi.app:app
     ```

Then, open your browser at [http://localhost:5000](http://localhost:5000).

---

## API Endpoint

### GET `/lookup`

#### Parameters

- **domain**: Domain name (required, e.g., `example.com`).
- **type**: DNS record type (optional, default is `A`).

#### Example Request

```http
GET /lookup?domain=example.com&type=MX
```

#### Success Response

```json
{
  "domain": "example.com",
  "record_type": "MX",
  "records": [
    "10 mail.example.com"
  ]
}
```

#### Error Responses

- **No Record Found:**

  ```json
  {
    "error": "No MX record found for example.com"
  }
  ```

- **Domain Does Not Exist:**

  ```json
  {
    "error": "Domain nonexistent.com does not exist."
  }
  ```

---

## Rate Limiting

Rate limiting is configured via the `.env` file (copy from `.env.example`):

- **Enabled:** By default.
- **Limits:** 5 requests per minute, 100 per hour, and 500 per day.
- **Per-Endpoint Limit:** 1 request per second.

To disable rate limiting, set in your `.env` file:

```env
ENABLE_RATE_LIMIT=False
```

---

## Supported Record Types

- **A:** IPv4 Address
- **AAAA:** IPv6 Address
- **MX:** Mail Exchange
- **TXT:** Text Record
- **CNAME:** Canonical Name
- **NS:** Name Server
- **SOA:** Start of Authority

---

## Credits

Built using:
- [dnspython](https://www.dnspython.org/) — DNS toolkit for Python.
- [Flask](https://flask.palletsprojects.com/) — Web framework.
- [Flask-Limiter](https://flask-limiter.readthedocs.io/) — Rate limiting.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

- [TheBiemGamer](https://github.com/TheBiemGamer)

---