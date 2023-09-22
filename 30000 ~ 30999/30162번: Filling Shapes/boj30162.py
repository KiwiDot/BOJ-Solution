# 백준 30162번 Filling Shapes
import sys
put = sys.stdin.readline

n = int(put())

if n % 2:
    print(0)
else:
    print(2 ** (n // 2))