
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# First, let's fix the index.html file
index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace protocol-relative URLs with local paths
    content = content.replace('//uk.tmconst.com/', '/uk.tmconst.com/')
    content = content.replace('https://uk.tmconst.com/', '/uk.tmconst.com/')
    content = content.replace('http://uk.tmconst.com/', '/uk.tmconst.com/')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed index.html URLs to use local paths!")

# Now start the server
PORT = 8000

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

try:
    with HTTPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped by user")
    httpd.server_close()
except Exception as e:
    print(f"Error starting server: {e}")
