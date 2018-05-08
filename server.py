#!/usr/bin/env python
import json

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

from swarm_node import send_transfer, get_tips, generate_address

from modules.tangleid import main as module_tangleid

PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        response = {
            'status':'SUCCESS',
            'data':'Hello I am a swarm node.'
        }

        self._set_headers()
        self.wfile.write(json.dumps(response))

    
    def do_POST(self):
        
        request_path = self.path
        
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        
        request_data = self.rfile.read(length)
        
        print "Get request data ... " + str(request_data)
	
        request_command = json.loads(request_data)

        if 'module' in request_command:
            if request_command['module'] == "tangleid":
                print "Result ... " + str(request_command['module'])
                result = load(request_data)
            else:
                result = "Error: Bad request"

        if request_command['command'] == "generate_address":
            result = generate_address()
        elif request_command['command'] == "get_tips":
            result = get_tips(int(request_command['type']))
        elif request_command['command'] == "send_transfer":
            if 'debug' not in request_command:
                debug = 0
            else:
                debug = int(request_command['debug'])

            dict_tips = get_tips(int(request_command['tips_type']))
            result = send_transfer(request_command['tag'], request_command['message'], \
                     request_command['address'], int(request_command['value']), dict_tips, debug)
        else:
            result = "Error: Bad request"
        
        print "Result ... " + str(result)

        self._set_headers()
        self.wfile.write(str(result))
    
def http_server():

    print "Listening on localhost:"  + str(PORT)
    server = HTTPServer(('', PORT), RequestHandler)
    server.serve_forever()

http_server()
