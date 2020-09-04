import SimpleHTTPServer
import SocketServer
import sys
import json

PORT = 1111 if len(sys.argv) == 1 else int(sys.argv[1])

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        json_str = self.rfile.read(length)
        parsed_json = json.loads(json_str)
        pretty_json = json.dumps(parsed_json, indent=2, sort_keys=True)
        print 'Device user agent:'
        print self.headers.getheader('user-agent')
        print
        print 'Features detected:'
        print pretty_json
        self.send_response(200)
        self.end_headers()

httpd = SocketServer.TCPServer(("", PORT), ServerHandler)

print "Serving HTTP on 0.0.0.0 port", PORT, "..."
httpd.serve_forever()
