# 백준 33612번 피갤컵
import sys
put = sys.stdin.readline

N = int(put())
y = 2024
m = 0 + N * 7

y += m // 12
m = m % 12 + 1

print(y, m)