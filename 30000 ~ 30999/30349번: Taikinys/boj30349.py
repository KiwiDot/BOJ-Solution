# 백준 30349번 Taikinys
import sys
put = sys.stdin.readline

M, N = map(int, put().split())
A, B = map(int, put().split())
X, Y = map(int, put().split())

answer = float('inf')
check = False

for m in range(M):
    for n in range(N):
        tx = m + X
        ty = n + Y
        if 0 <= tx < A and 0 <= ty < B:
            answer = min(answer, tx + ty)
            check = True

if check:
    print(answer)
else:
    print("NEPATAIKYS")
