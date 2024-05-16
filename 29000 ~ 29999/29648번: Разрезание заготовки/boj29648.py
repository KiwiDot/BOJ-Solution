# 백준 29648번 Разрезание заготовки
import sys
put = sys.stdin.readline

a, b, S = map(int, put().split())
L = (a + b + ((a + b) ** 2 - 4 * (a * b - S)) ** 0.5) / 2

print(int(L) if L.is_integer() else -1)