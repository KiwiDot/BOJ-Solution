# 백준 28940번 Дневник Гравити Фолз
import sys
from math import ceil
put = sys.stdin.readline

w, h = map(int, put().split())
n, a, b = map(int, put().split())

wi = w // a
hi = h // b

if not wi or not hi:
    print(-1)
else:
    p = wi * hi
    print(ceil(n / p))