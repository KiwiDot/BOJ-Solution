# 백준 29895번 Jõululaul
import sys
put = sys.stdin.readline

n = int(put())
for i in range(n):
    print((i+1) * (n-i))