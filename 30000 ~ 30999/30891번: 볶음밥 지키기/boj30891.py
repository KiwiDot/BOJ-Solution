# 백준 30891번 볶음밥 지키기
import sys
put = sys.stdin.readline

N, R = map(int, put().split())
data = [list(map(int, put().split())) for i in range(N)]
answer = {}

for X in range(-100, 101):
    for Y in range(-100, 101):
        cnt = 0

        for x, y in data:
            if (X - x) ** 2 + (Y - y) ** 2 <= R ** 2:
                cnt += 1

        if cnt:
            answer[cnt] = f"{X} {Y}"

print(answer[max(answer)])