# 백준 29644번 Прямоугольный полигон
import sys
put = sys.stdin.readline

S, P = map(int, put().split())
p = P // 2

if p ** 2 - S * 4 >= 0:
    a = (p + (p ** 2 - S * 4) ** 0.5) / 2
    b = p - a
    if a * b == S and a.is_integer() and b.is_integer():
        print(int(a), int(b))
    else:
        print(-1)
else:
    print(-1)