# 백준 30077번 Dviračių lenktynės
import sys
put = sys.stdin.readline

N, M, L = map(int, put().split())
T = [int(put()) for i in range(N)]
answer = 0
t = min(T)

for i in T:
    if i * (M-1) < t * M:
        answer += 1

print(answer)