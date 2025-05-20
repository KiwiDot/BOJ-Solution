# 백준 33964번 레퓨닛의 덧셈
import sys
put = sys.stdin.readline

X, Y = map(int, put().split())

print(eval(f"{'1' * X} + {'1' * Y}"))
