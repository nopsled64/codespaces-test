import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('.')


server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)

server_object.serve_forever()
print("Server is running")