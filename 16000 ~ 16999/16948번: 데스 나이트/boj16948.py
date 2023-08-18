# 백준 16948번 데스 나이트
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
r1, c1, r2, c2 = map(int, put().split())
visited = [[0] * N for i in range(N)]

visited[r1][c1] = 1
v = deque([(r1, c1, 0)])

while v:
    r, c, d = v.popleft()
    if r == r2 and c == c2:
        print(d)
        break

    for ri, ci in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
        if 0 <= ri < N and 0 <= ci < N and not visited[ri][ci]:
            visited[ri][ci] = 1
            v.append((ri, ci, d + 1))

else:
    print(-1)