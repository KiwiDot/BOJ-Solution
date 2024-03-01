# 백준 29721번 변형 체스 놀이 : 다바바(Dabbaba)
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
loc = {tuple(map(int, put().split())) for i in range(K)}
answer = set()

for X, Y in loc:
    for x, y in ((X+2, Y), (X-2, Y), (X, Y+2), (X, Y-2)):
        if 1 <= x <= N and 1 <= y <= N and (x, y) not in loc:
            answer.add((x, y))

print(len(answer))