#!/usr/bin/env python

import socket
import sys
import select

host = 'localhost'
src_port = 4000
dst_port = 4001


dst_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
dst_server_socket.setblocking(0)

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as src_socket:
    src_socket.bind((host, src_port))
    src_socket.listen()

    conn, addr = src_socket.accept() # accept TCP byte array
    with conn:
      print('Connected at {}'.format(addr))
      data = conn.recv(1024)
      print('Read {} bytes from Hermle.'.format(len(data)))
  dst_server_socket.sendto(data, (host, dst_port))
  print('send data to 4001')

finally:
  print('Closing all sockets now.')

  dst_server_socket.close()
