# 백준 33923번 인경호 울타리 공사
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
answer = 0

if N != M:
    answer = min(N-1, M-1) ** 2

n = min(N, M)
answer = max(answer, 1 + (n-2) ** 2)

print(answer)