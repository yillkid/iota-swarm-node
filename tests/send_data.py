import time
import json

import urllib2

HOST = 'http://127.0.0.1'
PORT = 8000

TIPS_TYPE_IRI_REQULAR_ALGORITHM = 0
TIPS_TYPE_TWO_NULL_IOTA_TNX = 1

tag = "PYTHONTEST"
message = "iHELLO"
address = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"
value = 0

url = str(HOST)+":"+str(PORT)

data = {
    'command' : 'send_transfer',
    'tag' : tag,
    'message' : message,
    'address' : address,
    'value' : value,
    'tips_type' : TIPS_TYPE_IRI_REQULAR_ALGORITHM,
    'debug' : 1
}


start = time.time()

print "Send send transfer command ... "

req = urllib2.Request(url)
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))

print "Response ... " + str(response.read())

end = time.time()
elapsed = end - start

print "Duration: " + str(elapsed) + " seconds"
