import time
import socket
import json

HOST = '127.0.0.1'
PORT = 8080

request_field = {
    "command" : "gen_a_address"
}

start = time.time()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

request_body = json.dumps(request_field)
print "Generating a unused address ... "
s.send(request_body)

data = s.recv(1024)
print data

s.close()

end = time.time()
elapsed = end - start

print "Duration: " + str(elapsed) + " seconds"
