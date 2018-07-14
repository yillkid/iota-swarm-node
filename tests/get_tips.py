#!/usr/bin/env python
import time
import json

import urllib.request
import urllib.parse

HOST = 'http://127.0.0.1'
PORT = 8000

url = str(HOST) + ":" + str(PORT)

TIPS_TYPE_IRI_REQULAR_ALGORITHM = 0
TIPS_TYPE_TWO_NULL_IOTA_TNX = 1

data = {
    "command": "get_tips",
    "type": TIPS_TYPE_IRI_REQULAR_ALGORITHM,
}

start = time.time()

print("Getting tips ...")

req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(req, json.dumps(data).encode('utf-8'))

print("Response ... %s" % (str(response.read())))

end = time.time()
elapsed = end - start

print("Duration: %s seconds" % (str(elapsed)))
