# 백준 29319번 Начало
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))

answer = sum(a) - max(a)
print(answer)