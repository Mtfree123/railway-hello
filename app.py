import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok", "service": "railway-hello"}).encode()
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
            self.wfile.write(body)
        else:
            body = b"<!doctype html><title>Railway Hello</title><h1>Railway Hello - deployment works</h1><p>This is a normal demo web app.</p><p><a href='/health'>/health</a></p>"
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
            self.wfile.write(body)
    def log_message(self, *a):
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    HTTPServer(("0.0.0.0", port), H).serve_forever()
