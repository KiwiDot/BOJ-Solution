# 백준 28812번 Доставка
import sys
put = sys.stdin.readline

n, C = map(int, put().split())
answer = float('inf')

while n:
    n -= 1
    p, d, v = map(int, put().split())
    answer = min(answer, p + d + v * C)

print(answer)
