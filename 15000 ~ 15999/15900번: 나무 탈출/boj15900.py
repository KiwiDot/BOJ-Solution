# 백준 15900번 나무 탈출
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
tree = dict([(i+1, []) for i in range(N)])

for i in range(N-1):
    a, b = map(int, put().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N+1)
visited[1] = 1
bfs = deque([(1, 0)])
answer = 0

while bfs:
    n, d = bfs.popleft()
    child_node = False

    for i in tree[n]:
        if not visited[i]:
            visited[i] = 1
            bfs.append((i, d+1))
            child_node = True

    if not child_node:
        answer += d

print("Yes" if answer % 2 else "No")