# 백준 28471번 W키가 빠진 성원이
import sys
from collections import deque
put = sys.stdin.readline

move = {'Q': (-1, -1), 'W': (-1, 0), 'E': (-1, 1), 'A': (0, -1),
        'D': (0, 1), 'Z': (1, 1), 'X': (1, 0), 'C': (1, -1)}

N = int(put())
game = []
x = y = 0

for i in range(N):
    data = list(put().strip())
    for j in range(N):
        if data[j] == 'F':
            x, y = i, j

    game.append(data)

answer = 0
bfs = deque([(x, y)])
game[x][y] = '#'

while bfs:
    x, y = bfs.popleft()

    for i in ['Q', 'W', 'E', 'A', 'D', 'Z', 'C']:
        dx, dy = move[i]
        if 0 <= x + dx < N and 0 <= y + dy < N and game[x + dx][y + dy] == '.':
            bfs.append((x + dx, y + dy))
            game[x + dx][y + dy] = 'F'
            answer += 1

print(answer)