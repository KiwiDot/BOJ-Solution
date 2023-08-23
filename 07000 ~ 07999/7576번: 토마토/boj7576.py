# 백준 7576번 토마토
import sys
put = sys.stdin.readline

M, N = map(int, put().split())
tomato = []
bfs = []

for i in range(N):
    data = put().split()
    for j in range(M):
        if data[j] == '1':
            bfs.append((i, j))
    tomato.append(data)

answer = -1
while bfs:
    answer += 1
    nxt = []
    for i, j in bfs:
        for n, m in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= n < N and 0 <= m < M and tomato[n][m] == '0':
                tomato[n][m] = '1'
                nxt.append((n, m))

    bfs = nxt

for i in tomato:
    if '0' in i:
        print(-1)
        break
else:
    print(answer)