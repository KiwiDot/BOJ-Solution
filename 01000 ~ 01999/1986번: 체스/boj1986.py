# 백준 1986번 체스
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
chess = [['-'] * m for i in range(n)]

Q = list(map(int, put().split()))
K = list(map(int, put().split()))
P = list(map(int, put().split()))

for i, t in [(Q, 'Q'), (K, 'K'), (P, 'P')]:
    d = i.pop(0)
    for j in range(0, d*2, 2):
        r, c = i[j] - 1, i[j+1] - 1
        chess[r][c] = t

for q in range(0, len(Q), 2):
    r, c = Q[q] - 1, Q[q+1] - 1
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        ri, cj = r, c

        while True:
            ri += i
            cj += j
            if 0 <= ri < n and 0 <= cj < m and (chess[ri][cj] == '-' or chess[ri][cj] == '!'):
                chess[ri][cj] = '!'
            else:
                break

for k in range(0, len(K), 2):
    r, c = K[k] - 1, K[k+1] - 1
    for i, j in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        ri, cj = r + i, c + j
        if 0 <= ri < n and 0 <= cj < m and (chess[ri][cj] == '-' or chess[ri][cj] == '!'):
                chess[ri][cj] = '!'

answer = 0
for i in chess:
    answer += i.count('-')
print(answer)