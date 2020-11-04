#!/usr/bin/python3 

buf = [0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0xa8, 0x81, 0xfd, 0xf7, 0x0, 0xd0, 0xff, 0xf7, 0x3b, 0x6d, 0xfe, 0xf7, 0x0, 0xc0, 0xff, 0xf7, 0x0, 0x10, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0xfc, 0x6c, 0xfe, 0xf7, 0x0, 0xd0, 0xff, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x18, 0xd6, 0xff, 0xff, 0x4b, 0x72, 0xfe, 0xf7, 0xf0, 0xda, 0xff, 0xf7, 0x60, 0x87, 0xfd, 0xf7, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x8c, 0x57, 0xff, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5c, 0xd5, 0xff, 0xf7, 0xe8, 0xd5, 0xff, 0xff, 0x8, 0xd6, 0xff, 0xff, 0x0, 0x0, 0x0, 0x0, 0x8c, 0x57, 0xff, 0xf7, 0x5c, 0xd5, 0xff, 0xf7, 0x8, 0xd6, 0xff, 0xff, 0xac, 0xc4, 0xfd, 0xf7, 0xdc, 0xc2, 0xfd, 0xf7, 0x3d, 0x4f, 0xfe, 0xf7, 0x61, 0x60, 0xe3, 0xf7, 0xff, 0x82, 0x4, 0x8, 0x0, 0x0, 0x0, 0x0, 0x3c, 0xc3, 0xfd, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x0, 0xc0, 0xfd, 0xf7, 0x40, 0x0, 0x0, 0x0, 0x2, 0x0, 0x0, 0x0, 0x7d, 0x82, 0x4, 0x8, 0x24, 0xdc, 0xff, 0xf7, 0xbc, 0x26, 0xe2, 0xf7, 0x0, 0xd0, 0xff, 0xf7, 0xc4, 0x6c, 0xe2, 0xf7, 0x1, 0x0, 0x0, 0x0, 0x60, 0x84, 0xfd, 0xf7, 0x94, 0x56, 0xfe, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x60, 0x84, 0xfd, 0xf7, 0x3, 0x0, 0x0, 0x0, 0x30, 0xd6, 0xff, 0xff, 0x71, 0xea, 0xb1, 0x7, 0x2e, 0x4e, 0x3d, 0xf6, 0xd4, 0x6e, 0xe2, 0xf7, 0x34, 0xfc, 0xe2, 0xf7, 0xb6, 0xe, 0xff, 0xf7, 0x0, 0xd0, 0xff, 0xf7, 0x77, 0x4, 0xfe, 0xf7, 0x5c, 0xd5, 0xff, 0xf7, 0xf0, 0xda, 0xff, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0xd6, 0x8, 0x0, 0x0, 0x90, 0x84, 0xfd, 0xf7, 0xa8, 0x81, 0xfd, 0xf7, 0xd4, 0x82, 0x4, 0x8, 0x74, 0x4, 0xe3, 0xf7, 0x5c, 0x82, 0x4, 0x8, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2, 0x0, 0x86, 0x30, 0xff, 0xf7, 0x2, 0x0, 0x0, 0x0, 0x0, 0xd0, 0xff, 0xf7, 0x74, 0xd7, 0xff, 0xff, 0xf0, 0xda, 0xff, 0xf7, 0x30, 0xd7, 0xff, 0xff, 0x1a, 0x59, 0xfe, 0xf7, 0xe0, 0xd6, 0xff, 0xff, 0x5c, 0x82, 0x4, 0x8, 0xe8, 0xd6, 0xff, 0xff, 0x94, 0xda, 0xff, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x90, 0x84, 0xfd, 0xf7, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x38, 0xd9, 0xff, 0xf7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x21, 0x0, 0x0, 0x0, 0x9, 0x0, 0x0, 0x0, 0x4d, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x74, 0xd7, 0xff, 0xff, 0xe8, 0xd6, 0xff, 0xff, 0xe0, 0xd6, 0xff, 0xff, 0xd4, 0x82, 0x4, 0x8, 0x38, 0xd9, 0xff, 0xf7, 0x0, 0x0, 0x0, 0x0, 0xc2, 0x0, 0x0, 0x0, 0x0, 0x91, 0xeb, 0xf7, 0xff, 0xff, 0xff, 0xff, 0xe, 0xd7, 0xff, 0xff, 0x34, 0xfc, 0xe2, 0xf7, 0xe3, 0x5f, 0xe5, 0xf7, 0x4d, 0x0, 0x0, 0x0, 0x7d, 0x30, 0x2c, 0x0, 0x1, 0x0, 0x0, 0x0, 0xa9, 0x83, 0x4, 0x8, 0xfd, 0xd8, 0xff, 0xff, 0x2f, 0x0, 0x0, 0x0, 0x0, 0xa0, 0x4, 0x8, 0x22, 0x87, 0x4, 0x8, 0x1, 0x0, 0x0, 0x0, 0xd4, 0xd7, 0xff, 0xff, 0xdc, 0xd7, 0xff, 0xff, 0x9d, 0x61, 0xe5, 0xf7, 0xc4, 0xd3, 0xfc, 0xf7, 0x0, 0xd0, 0xff, 0xf7, 0xdb, 0x86, 0x4, 0x8] 

print(len(buf))
print(buf[len(buf)//2])
