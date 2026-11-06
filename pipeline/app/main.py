from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def simple_interest(principal, rate, years):
    return round(principal * rate * years / 100, 2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "ok", "version": "v2",
                           "demo_interest": simple_interest(10000, 7, 2)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
