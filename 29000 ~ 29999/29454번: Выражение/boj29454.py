# 백준 29454번 Выражение
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))

check = sum(a)
for i in range(n):
    if a[i] * 2 == check:
        print(i + 1)
        break