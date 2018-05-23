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


# A5 A5 A5 A5 A5 A5 A5 A5
# fe ff 00 80 f0 00 fe ff 00 00 00 00 0E 00 00 00
# 01 a9 01 00 00 50 30 30 30 00 00 01 00 01
# 3C 65
# 5a
import struct

if __name__ == "__main__":
    RtnReq = 0x01
    CmdGroup = 0xA9
    Cmd = 0x01
    Reserved = 0x0
    BlockUnit = "P000"

    part_1 = struct.pack("QHHBBHIIBBBBB4s", 0xA5A5A5A5A5A5A5A5, 0xfffe, 0x8000, 0xf0, 0x00, 0xfffe, 0x0, 0x0e,
                         RtnReq, CmdGroup, Cmd, Reserved, Reserved, BlockUnit)
    print " ".join([hex(ord(x)) for x in part_1])

    # crc = 1
    # cmd = struct.pack("8B16B14B", frame_header, packet_header, data, crc, 0x5A)
    # print " ".join([hex(ord(x)) for x in cmd])
    # send_cmd(cmd)
