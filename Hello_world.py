<<<<<<< ours
print("hello world")
=======
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), HelloHandler)
    print("Server running at http://127.0.0.1:8000")
    server.serve_forever()
>>>>>>> theirs
