# 백준 28786번 Выстрел в голову
import sys
put = sys.stdin.readline

n, m, a, b = map(int, put().split())
answer = []

for i in range(n // m + 2):
    ai = a * i
    bi = b * (n - m * i) if n > m * i else 0

    answer.append(ai + bi)

print(min(answer) + n)