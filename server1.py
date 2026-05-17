import socketserver
import os

import http.server

PORT = 8000
DIRECTORY = "/Users/leonielettenbichler/Documents/Website"

os.chdir(DIRECTORY)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server läuft auf http://localhost:{PORT}")
    httpd.serve_forever()
    