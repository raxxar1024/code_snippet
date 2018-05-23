# -*- coding: utf-8 -*-
from socket import *

HOST = '192.168.1.92'
PORT = 5005
BUFSIZE = 1024
ADDR = (HOST, PORT)


def send_cmd(cmd):
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        tcpCliSock.send(cmd)
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print data
    tcpCliSock.close()


if __name__ == "__main__":
    RtnReq = 0x01
    CmdGroup = 0xA9
    Cmd = 0x01
    Reserved = 0x0000
    BlockUnit = 0x1
    import struct

    cmd = struct.pack(">BBBHB", RtnReq, CmdGroup, Cmd, Reserved, BlockUnit)
    print " ".join([hex(ord(x)) for x in cmd])
    send_cmd(cmd)
