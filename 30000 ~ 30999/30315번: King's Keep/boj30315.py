# 백준 30315번 King's Keep
import sys
put = sys.stdin.readline

k = int(put())
xy = [list(map(int, put().split())) for i in range(k)]
answer = set()

for x, y in xy:
    d = 0
    for xi, yi in xy:
        d += ((x - xi) ** 2 + (y - yi) ** 2) ** 0.5

    answer.add(d / (k-1))
print(min(answer))