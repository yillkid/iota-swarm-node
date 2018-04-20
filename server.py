import socket
import json

from swarm_node import send_transfer, get_tips, gen_a_address

HOST = '0.0.0.0'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(0)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'
result = ""
while True:
    conn, addr = s.accept()
    print 'Connected by ', addr

    while True:
        data = conn.recv(1024)
        request_command = json.loads(data)

        if request_command['command'] == "gen_a_address":
            result = gen_a_address()
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

        conn.send(str(result))
        break

conn.close()
