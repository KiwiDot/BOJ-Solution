# 백준 31589번 포도주 시음
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
T = sorted(list(map(int, put().split())))
answer = wine = 0

for i in range(K):
    if i % 2:
        wine = T[i//2]
    else:
        answer += T[-i//2-1] - wine
        wine = T[-i//2-1]

print(answer)