import time
import socket
import json

HOST = '127.0.0.1'
PORT = 8080

TIPS_TYPE_IRI_REQULAR_ALGORITHM = 0
TIPS_TYPE_TWO_NULL_IOTA_TNX = 1

tag = "PYTHONTEST"
message = "HELLO"
address = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"
value = 0

request_field = {
    "command" : "send_transfer",
    "tag" : tag,
    "message" : message,
    "address" : address,
    "value" : value,
    "tips_type" : TIPS_TYPE_IRI_REQULAR_ALGORITHM
}

start = time.time()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

request_body = json.dumps(request_field)
print "Send send transfer command ... "
s.send(request_body)

data = s.recv(1024)
print data

s.close()

end = time.time()
elapsed = end - start

print "Duration: " + str(elapsed) + " seconds"
