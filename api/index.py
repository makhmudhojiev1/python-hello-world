from http.server import BaseHTTPRequestHandlerclass handler(BaseHTTPRequestHandler): def do_GET(self): self.send_response(200) self.send_header('Content-type','text/plain') self.end_headers() self.wfile.write('Hello, wsasasorld!'.encode('utf-8')) return
