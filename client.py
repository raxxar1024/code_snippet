# -*- coding: utf-8 -*-

import socket
import struct

PORT = 8000
HOST = '192.168.1.249'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# tmp_bytes = struct.pack('19B', 0x10, 0x50, 0x01, 0x01, 0x02, 0xd, 0xa, 0x28, 0x7,
#                         0x8, 0x0, 0xc8, 0x0, 0xc3, 0x50, 0x0, 0x0, 0x5, 0xff)
tmp_bytes = struct.pack('6B', 0x10, 0x03, 0x01, 0x01, 0x02, 0x0)

s.send(tmp_bytes)

buf = s.recv(1024)
print "dataReceived <--- "+" ".join([hex(ord(x)) for x in buf])
s.close()
