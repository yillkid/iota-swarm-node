import time
import socket
import json

HOST = '127.0.0.1'
PORT = 8080

TIPS_TYPE_IRI_REQULAR_ALGORITHM = 0
TIPS_TYPE_TWO_NULL_IOTA_TNX = 1

request_field = {
    "command" : "get_tips",
    "type" : TIPS_TYPE_IRI_REQULAR_ALGORITHM,
}

start = time.time()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

request_body = json.dumps(request_field)
print "Getting tips ..."
s.send(request_body)

data = s.recv(1024)
print data

s.close()

end = time.time()
elapsed = end - start

print "Duration: " + str(elapsed) + " seconds"
