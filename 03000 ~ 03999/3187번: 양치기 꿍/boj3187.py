# 백준 3187번 양치기 꿍
import sys
from collections import deque
put = sys.stdin.readline

R, C = map(int, put().split())
farm = [list(put().strip()) for i in range(R)]

answer = {'k': 0, 'v': 0}
for i in range(R):
    for j in range(C):
        if farm[i][j] == '#':
            continue

        cnt = {'k': 0, 'v': 0, '.': 0}
        cnt[farm[i][j]] += 1
        farm[i][j] = '#'

        bfs = deque([(i, j)])
        while bfs:
            ii, jj = bfs.popleft()

            for r, c in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                if 0 <= r < R and 0 <= c < C and farm[r][c] != '#':
                    cnt[farm[r][c]] += 1
                    farm[r][c] = '#'
                    bfs.append((r, c))

        if cnt['k'] > cnt['v']:
            answer['k'] += cnt['k']
        else:
            answer['v'] += cnt['v']

print(answer['k'], answer['v'])