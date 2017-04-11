#!/usr/bin/env python
import sys
print(sys.argv[1])
while 1:
    buf = sys.stdin.read(2048)
    if not buf: break
    sys.stdout.write(buf)
print(sys.argv[1])
