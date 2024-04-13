# 백준 21529번 Кастинг
import sys
put = sys.stdin.readline

k = int(put())
n, a, b, c = map(int, put().split())

if k == 1:
    print(max(a + b + c - 2 * n, 0))

else:
    print(min(a, b, c))