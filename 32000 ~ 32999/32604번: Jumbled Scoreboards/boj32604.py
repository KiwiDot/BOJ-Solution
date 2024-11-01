# 백준 32604번 Jumbled Scoreboards
import sys
put = sys.stdin.readline

n = int(put())
A, B = [], []

while n:
    n -= 1
    a, b = map(int, put().split())
    A.append(a)
    B.append(b)

if A == sorted(A) and B == sorted(B):
    print("yes")
else:
    print("no")