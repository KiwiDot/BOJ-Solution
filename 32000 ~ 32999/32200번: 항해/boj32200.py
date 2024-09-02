# 백준 32200번 항해
import sys
put = sys.stdin.readline

N, X, Y = map(int, put().split())
A = list(map(int, put().split()))
answer = [0, 0]

for i in A:
    a = i // X
    answer[0] += a
    answer[1] += max(0, i - a * Y)

for i in answer:
    print(i)