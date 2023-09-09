# 백준 28598번 Пилтовер и Заун
import sys
put = sys.stdin.readline

x1, x2, n = map(int, put().split())

x = (x1 + x2) // 2

if x1 - x == x - x2 and x1 - x >= n:
    print("YES")
else:
    print("NO")