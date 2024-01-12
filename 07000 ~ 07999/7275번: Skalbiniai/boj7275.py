# 백준 7275번 Skalbiniai
import sys
from math import ceil
put = sys.stdin.readline

N, K, M = map(int, put().split())
data = [list(map(int, put().split()))[1:] for i in range(K)]
D = list(map(int, put().split()))

answer = 0
for i in data:
    G = sum([D[j - 1] for j in i])
    answer += ceil(G / M)

print(answer)