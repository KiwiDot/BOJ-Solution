# 백준 29009번 Поход в кино
import sys
put = sys.stdin.readline

N, A, B = map(int, put().split())
n = N // 2

a = [i for i in range(N) if not n - A < i < n + A]
b = [i for i in range(N) if not n - B < i < n + B]

print(max(len(a) * len(b) - 1, 0))