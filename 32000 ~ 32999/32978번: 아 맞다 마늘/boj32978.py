# 백준 32978번 아 맞다 마늘
import sys
put = sys.stdin.readline

N = int(put())

a = set(put().split())
b = set(put().split())

print(list(a - b)[0])