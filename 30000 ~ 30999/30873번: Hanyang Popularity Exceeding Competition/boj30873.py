# 백준 30873번 Hanyang Popularity Exceeding Competition
import sys
put = sys.stdin.readline

N = int(put())
X = 0

while N:
    N -= 1
    P, C = map(int, put().split())
    if abs(P - X) <= C:
        X += 1

print(X)