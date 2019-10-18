from http import server
from urllib.parse import unquote
import base64
from time import gmtime, strftime

class Handler(server.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length'))
        print("post", length)
        data = unquote(str(self.rfile.read(length)))
        png = data.split('base64,')[1]

        filename = strftime("%Y-%m-%d_%H-%M-%S.png", gmtime())

        with open(filename, "wb") as f:
            f.write(base64.decodestring(png.encode()))

        self.send_response(server.HTTPStatus.OK)
        self.end_headers()

def run(server_class=server.HTTPServer,
        handler_class=Handler):

    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
