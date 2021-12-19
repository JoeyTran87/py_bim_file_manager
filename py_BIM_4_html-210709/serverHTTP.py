import http
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler

# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('', 8000)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()

class ecoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())
def main():
    PORT = 8000
    server = HTTPServer(('', PORT),ecoHandler)
    print('Server runing on port: %s'%PORT)
    print('Press Ctrl + C for QUIT')
    server.serve_forever()

if __name__ == '__main__':
    main()