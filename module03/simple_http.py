from http.server import HTTPServer, BaseHTTPRequestHandler

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Hello world</h1>
</body>
</html>
"""



class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


server = HTTPServer(("", 8000), HttpHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
