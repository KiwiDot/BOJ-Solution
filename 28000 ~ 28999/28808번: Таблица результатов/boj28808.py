# 백준 28808번 Таблица результатов
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
answer = 0

while n:
    n -= 1
    data = put().strip()
    if '+' in data:
        answer += 1

print(answer)