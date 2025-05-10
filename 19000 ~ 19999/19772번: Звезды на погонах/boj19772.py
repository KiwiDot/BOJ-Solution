# 백준 19772번 Звезды на погонах
import sys
put = sys.stdin.readline

a, b, c, d, e = map(int, put().split())
n = 0

n += (c - e) - a
n += min(b, c-1) - (c - d)

m = {i for i in range(a, b+1)}
cd = c - d
ce = c - e

m -= {cd, ce}

print(n, len(m))