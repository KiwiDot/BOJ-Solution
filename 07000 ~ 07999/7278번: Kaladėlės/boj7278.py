# 백준 7278번 Kaladėlės
import sys
from math import ceil
put = sys.stdin.readline

N = int(put())
a, b, c = map(int, put().split())
answer = []

for n in [a, b, c]:
    n1 = N // n * n
    n2 = ceil(N / n) * n

    answer.append([n, n1])
    answer.append([n, n2])


answer.sort(key=lambda x: abs(N - x[1]))
print(*answer[0])