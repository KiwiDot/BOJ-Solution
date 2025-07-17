# 백준 28969번 Путешествие сквозь миры
import sys
put = sys.stdin.readline

l, r = map(int, put().split())
answer = 0

for i in range(1, 19):
    for j in range(1, 10):
        n = int(str(j) * i)
        if l <= n <= r:
            answer += 1

print(answer)
