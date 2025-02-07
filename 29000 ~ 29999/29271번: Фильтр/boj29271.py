# 백준 29271번 Фильтр
import sys
put = sys.stdin.readline

n, r, x = map(int, put().split())
a = list(map(int, put().split()))
answer = oil = 0

for i in a:
    oil += i
    o = max(0, oil - r)
    oil -= o

    o = min(x, oil)
    answer += o
    oil -= o

print(answer)