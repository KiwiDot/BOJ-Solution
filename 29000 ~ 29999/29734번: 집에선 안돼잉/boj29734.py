# 백준 29734번 집에선 안돼잉
import sys
from math import ceil
put = sys.stdin.readline

N, M = map(int, put().split())
T, S = map(int, put().split())

n = ceil(N / 8) - 1
m = ceil(M / 8) - 1

Zip = N + n * S
Dok = M + m * S + m * T * 2 + T

if Zip < Dok:
    print("Zip")
    print(Zip)

else:
    print("Dok")
    print(Dok)