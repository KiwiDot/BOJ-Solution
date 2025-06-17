# 백준 34027번 제곱 수?
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())
    print(int(int(N ** 0.5) ** 2 == N))