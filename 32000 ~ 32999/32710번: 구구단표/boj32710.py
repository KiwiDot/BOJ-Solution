# 백준 32710번 구구단표
import sys
put = sys.stdin.readline

num = {1}

for A in range(2, 10):
    for B in range(1, 10):
        num.add(A * B)

N = int(put())

print(1 if N in num else 0)