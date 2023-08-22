# 백준 6118번 숨바꼭질
import sys
from collections import deque
put = sys.stdin.readline

N, M = map(int, put().split())
graph = dict([(i+1, []) for i in range(N)])

while M:
    M -= 1
    A, B = map(int, put().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [0] * (N+1)
visited[1] = 1
bfs = deque([(1, 0)])
answer = {}

while bfs:
    n, d = bfs.popleft()
    if d in answer:
        answer[d].append(n)
    else:
        answer[d] = [n]

    for i in graph[n]:
        if not visited[i]:
            visited[i] = 1
            bfs.append((i, d+1))

max_d = max(answer)
print(min(answer[max_d]), max_d, len(answer[max_d]))