#!/usr/bin/env python
from service import generate_address

HOST = 'http://127.0.0.1'
PORT = 8000
url = str(HOST) + ":" + str(PORT)

generate_address(url)
