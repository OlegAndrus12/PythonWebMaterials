from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import mimetypes

BASE_DIR = Path()

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_html_file("index.html")
        elif self.path == "/blog":
            self.send_html_file("blog.html")
        elif self.path == "/contact":
            self.send_html_file("contact.html")
        else:
            filename = BASE_DIR.joinpath(self.path[1:])
            if filename.exists():
                self.send_static(filename)
            else:
                self.send_html_file("404.html", 404)
    
    
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()
    
    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as f:
            self.wfile.write(f.read())

    def send_static(self, filename, status=200):
        mt = mimetypes.guess_type(self.path)
        self.send_response(status)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        with open(filename, "rb") as f:
            self.wfile.write(f.read())





server = HTTPServer(("", 8000), HttpHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
