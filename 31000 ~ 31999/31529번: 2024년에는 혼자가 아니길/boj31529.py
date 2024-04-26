# 백준 31529번 2024년에는 혼자가 아니길
import sys
put = sys.stdin.readline

X, Y = map(int, put().split())

print((X * 2 - Y) * 506 if X <= Y <= X * 2 else -1)