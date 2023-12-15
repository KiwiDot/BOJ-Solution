# 백준 30767번 Dungeons & Dragons
import sys
put = sys.stdin.readline

n, a, b, c, d = [int(put()) for i in range(5)]

if a + c <= n <= b + d:
    ai = max(n - d, a)
    bi = min(n - c, b)
    print(bi - ai + 1)
else:
    print(0)