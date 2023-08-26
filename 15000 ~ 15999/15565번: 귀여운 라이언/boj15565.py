# 백준 15565번 귀여운 라이언
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
doll = list(map(int, put().split()))

Ryan = []
answer = set()
for i in range(N):
    if doll[i] == 1:
        Ryan.append(i)

        if len(Ryan) >= K:
            answer.add(Ryan[-1] - Ryan[-K] + 1)

print(min(answer) if answer else -1)
