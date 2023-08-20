from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os

# Define the server host and port
HOST_NAME = 'localhost'
PORT_NUMBER = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, 'Not Found')

    def do_POST(self):
        if self.path == '/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(post_data)

            name = form_data.get('name', [''])[0]
            email = form_data.get('email', [''])[0]

            # Save or process the registration data as needed
            # Here, you can add your logic to store the registration details

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Registration successful!'.encode('utf-8'))
        else:
            self.send_error(404, 'Not Found')

if __name__ == '__main__':
    server = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print(f'Server started on http://{HOST_NAME}:{PORT_NUMBER}/')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print('Server stopped')
