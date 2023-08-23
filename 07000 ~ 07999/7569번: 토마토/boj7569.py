# 백준 7569번 토마토
import sys
put = sys.stdin.readline

M, N, H = map(int, put().split())
tomato = []
bfs = []

for h in range(H):
    tomato.append([])
    for n in range(N):
        data = put().split()
        for m in range(M):
            if data[m] == '1':
                bfs.append((h, n, m))
        tomato[-1].append(data)

answer = -1
while bfs:
    answer += 1
    nxt = []

    for i, j, k in bfs:
        for h, n, m in [(i-1, j, k), (i+1, j, k), (i, j-1, k), (i, j+1, k), (i, j, k-1), (i, j, k+1)]:
            if 0 <= h < H and 0 <= n < N and 0 <= m < M and tomato[h][n][m] == '0':
                tomato[h][n][m] = '1'
                nxt.append((h, n, m))

    bfs = nxt

for i in tomato:
    for j in i:
        if '0' in j:
            answer = -1

print(answer)