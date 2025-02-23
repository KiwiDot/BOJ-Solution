# 백준 19752번 Большой круглый стол
import sys
put = sys.stdin.readline

n, k = map(int, put().split())

if n % 2 == 1:
    print(min(n, k + 1))
else:
    print(min(n // 2, k + 1))
