# 백준 34125번 래환이의 아이브 콘서트 이야기
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = [list(map(int, put().split())) for i in range(N)]
answer = {}

for R in range(1, N+1):
    for C in range(1, M+1):
        if data[R-1][C-1]:
            continue

        answer[f"{R} {C}"] = R + abs((M + 1) // 2 - C)

if answer:
    print(min(answer, key=answer.get))
else:
    print(-1)