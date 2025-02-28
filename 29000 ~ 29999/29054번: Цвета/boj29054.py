# 백준 29054번 Цвета
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))

print(max(a) - min(a) + 1)