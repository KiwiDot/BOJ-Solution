# 백준 18290번 NM과 K (1)
import sys
put = sys.stdin.readline


def solution(loc, k):
    global N, M, K
    if k == K:
        n = sum([data[i][j] for i, j in loc])
        answer.add(n)

    else:
        if loc:
            i, j = loc[-1]
            idx = i * M + j
        else:
            idx = 0

        for x in range(idx, N * M):
            i, j = divmod(x, M)
            if not visited[i][j] and not {(i-1, j), (i, j-1)} & set(loc):
                visited[i][j] = 1
                solution(loc + [(i, j)], k + 1)
                visited[i][j] = 0


N, M, K = map(int, put().split())
data = [list(map(int, put().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]
answer = set()

solution([], 0)
print(max(answer))