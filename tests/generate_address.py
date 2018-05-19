#!/usr/bin/env python
import time
import json

import urllib2

HOST = 'http://127.0.0.1'
PORT = 8000

url = str(HOST)+":"+str(PORT)

data = {
    "command" : "generate_address"
}

start = time.time()

print "Generating a unused address ... "

req = urllib2.Request(url)
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))

print "Response ... " + str(response.read())

end = time.time()
elapsed = end - start

print "Duration: " + str(elapsed) + " seconds"
