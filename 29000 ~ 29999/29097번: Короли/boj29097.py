# 백준 29097번 Короли
import sys
put = sys.stdin.readline

n, m, k, a, b, c = map(int, put().split())
check = max(n * a, m * b, k * c)
answer = []

for i in [("Joffrey", n * a), ("Robb", m * b), ("Stannis", k * c)]:
    if i[1] == check:
        answer.append(i[0])

print(*answer)