# 백준 31800번 Best Chance
import sys
put = sys.stdin.readline

N = int(put())
p = list(map(int, put().split()))
price = list(map(int, put().split()))

price_sort = sorted(p, reverse=True)[:2]
answer = []

for i in range(N):
    if p[i] == price_sort[0]:
        answer.append(p[i] - price_sort[1])
    else:
        answer.append(p[i] - price_sort[0])

print(*answer)