#!/usr/bin/env python3 

import socket
import struct 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "vortex.labs.overthewire.org"
port = 5842

s.connect((host, port))

total = 0

for i in range(4):
    num = s.recv(4)
    unpacked = struct.unpack("<I", num)
    print(unpacked)
    total += unpacked[0]

s.send(struct.pack("<I", total & 0xffffffff))
print(s.recv(1024))
