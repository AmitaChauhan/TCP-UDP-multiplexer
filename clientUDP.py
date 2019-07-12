#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT1 = 4001      # The port used by the server


client_address = (HOST, PORT1)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(client_address)

    print('I am a UDP client')
    data = s.recvfrom(4001)
    print(data)
