from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Python Server!")

HOST = "0.0.0.0"
PORT = 8000
PORT = 5000

server = HTTPServer((HOST, PORT), MyHandler)

print(f"Server is running on http://{HOST}:{PORT}")

server.serve_forever()
