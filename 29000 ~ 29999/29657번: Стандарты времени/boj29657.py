# 백준 29657번 Стандарты времени
import sys
put = sys.stdin.readline

a1, b1, c1 = map(int, put().split())
a2, b2, c2 = map(int, put().split())
h1, m1, s1 = map(int, put().split())

t1 = h1 * b1 * c1 + m1 * c1 + s1

h2, t1 = divmod(t1, b2 * c2)
m2, s2 = divmod(t1, c2)
print(h2, m2, s2)