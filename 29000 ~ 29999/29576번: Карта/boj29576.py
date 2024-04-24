# 백준 29576번 Карта
import sys
put = sys.stdin.readline

n, k = map(lambda x: int(x) - 1, put().split())

if k:
    print(-1 if n % k else n // k)
else:
    print(int(not bool(n)) - 1)