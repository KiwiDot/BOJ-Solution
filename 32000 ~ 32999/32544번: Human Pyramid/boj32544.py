# 백준 32544번 Human Pyramid
import sys
put = sys.stdin.readline

n = int(put())

for i in range(1, 10 ** 7):
    k = i * (i + 1) // 2
    if k > n:
        print(i - 1)
        break