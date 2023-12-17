# 백준 11060번 점프 점프
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

path = [[] for i in range(N)]
answer = [0] * N
path[0].append(-1)

for i in range(N):
    if path[i]:
        answer[i] = min(path[i]) + 1
        for j in range(1, A[i] + 1):
            if i + j >= N:
                break
            path[i + j].append(answer[i])
    else:
        answer[i] = -1

print(answer[-1])
