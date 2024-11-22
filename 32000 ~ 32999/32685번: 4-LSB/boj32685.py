# 백준 32685번 4-LSB
import sys
put = sys.stdin.readline

a = bin(int(put()))[2:].zfill(4)[-4:]
b = bin(int(put()))[2:].zfill(4)[-4:]
c = bin(int(put()))[2:].zfill(4)[-4:]

print(str(int(a + b + c, 2)).zfill(4))