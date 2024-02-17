# 백준 24511번 queuestack
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
B = list(map(int, put().split()))

M = int(put())
C = list(map(int, put().split()))
answer = ([B[i] for i in range(N) if not A[i]][::-1] + C)[:M]

print(*answer)