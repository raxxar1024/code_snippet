# -*- coding: utf-8 -*-

import socket

port = 8081
host = '192.168.1.91'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('hello,this is a test info!', (host, port))

# time.sleep(1)
# reply = s.recv(4096)
# print reply
