# Subdomain Enumerator (Python)

A simple multithreaded subdomain enumeration tool built using Python and ThreadPoolExecutor.

This project was created to understand concurrency, thread pools, futures, and HTTP-based subdomain discovery.

---

##  Features

- Multithreaded scanning using ThreadPoolExecutor
- Custom thread count
- HTTPS-based subdomain checking
- HTTP status code differentiation (200, 301, 302, 403, 404, etc.)
- Graceful exception handling
- Clean terminal output


## 🧠How It Works

1. Loads a wordlist of possible subdomains.
2. Constructs URLs in the format:

   https://subdomain.target.com

3. Sends HTTP requests concurrently.
4. Prints discovered subdomains along with their status codes.

---

##  Requirements

- Python 3.x
- requests library

Install dependencies:

```bash
pip install -r requirements.txt
