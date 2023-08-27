# 백준 29558번 Эксперимент
import sys
put = sys.stdin.readline

N, D = map(int, put().split())
answer = []

for i in range(N // 2):
    answer.append(D - i - 1)
    answer.append(D + i + 1)

if N % 2:
    answer.append(D)

print(*sorted(answer))