# 백준 31868번 수박 게임
import sys
put = sys.stdin.readline

N, K = map(int, put().split())

for i in range(N-1):
    K //= 2

print(K)