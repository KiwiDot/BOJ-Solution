# 백준 32813번 Oooh I See
import sys
put = sys.stdin.readline

r, c = map(int, put().split())
grid = [put().strip() for i in range(r)]

answer = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(1, r-1):
    for j in range(1, c-1):
        if grid[i][j] == '0':
            for k in range(8):
                ni = dx[k] + i
                nj = dy[k] + j
                if grid[ni][nj] != 'O':
                    break
            else:
                answer.append((i+1, j+1))

if len(answer) == 0:
    print("Oh no!")
elif len(answer) == 1:
    print(*answer[0])
else:
    print(f"Oh no! {len(answer)} locations")
