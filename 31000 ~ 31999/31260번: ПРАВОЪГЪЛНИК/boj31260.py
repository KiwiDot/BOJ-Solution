# 백준 31260번 ПРАВОЪГЪЛНИК
import sys
put = sys.stdin.readline

x, y = map(int, put().split())
d = int(put())

l = (x * 100 + y) // 2

a = (l - d) // 2 + d
b = (l - d) // 2

print(a // 100, a % 100)
print(b // 100, b % 100)