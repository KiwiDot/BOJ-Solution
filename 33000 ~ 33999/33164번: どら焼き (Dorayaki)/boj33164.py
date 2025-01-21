# 백준 33164번 どら焼き (Dorayaki)
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = list(map(int, put().split()))
B = list(map(int, put().split()))

answer = 0
for a in A:
    for b in B:
        answer += (a + b) * max(a, b)

print(answer)