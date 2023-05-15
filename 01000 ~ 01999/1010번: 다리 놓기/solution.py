# 백준 1010번 다리 놓기
import sys
from math import comb
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N, M = map(int, put().split())

    print(comb(M, N))
