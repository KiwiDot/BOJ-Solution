# 백준 16507번 어두운 건 무서워
import sys
put = sys.stdin.readline

R, C, Q = map(int, put().split())
K = [list(map(int, put().split())) for i in range(R)]
data = [[0] * C for i in range(R)]

for i in range(R):
    for j in range(C):
        r = data[i-1][j] if i > 0 else 0
        c = data[i][j-1] if j > 0 else 0
        rc = data[i-1][j-1] if i > 0 and j > 0 else 0
        data[i][j] = r + c + K[i][j] - rc

while Q:
    Q -= 1
    r1, c1, r2, c2 = [int(i) - 1 for i in put().split()]
    r = data[r1-1][c2] if r1 > 0 else 0
    c = data[r2][c1-1] if c1 > 0 else 0
    rc = data[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0

    n = (r2 - r1 + 1) * (c2 - c1 + 1)
    answer = (data[r2][c2] - r - c + rc) // n
    print(answer)

