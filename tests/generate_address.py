#!/usr/bin/env python
import time
import json

import urllib.request
import urllib.parse

HOST = 'http://127.0.0.1'
PORT = 8000

url = str(HOST) + ":" + str(PORT)

data = {
    "command": "generate_address"
}

start = time.time()

print("Generating an unused address ... ")

req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json')

response = urllib.request.urlopen(req, json.dumps(data).encode('utf-8'))

print("Response ... %" % (str(response.read())))

end = time.time()
elapsed = end - start

print("Duration: %s seconds" % (str(elapsed)))
