# 백준 29133번 Фома и занимательная математика
import sys
put = sys.stdin.readline

a, b, c, d = map(int, put().split())
answer = []

for x in range(1, 4):
    if a ** x + b ** x + c ** x == d:
        answer.append(x)

print(answer[0] if len(answer) == 1 else -1)