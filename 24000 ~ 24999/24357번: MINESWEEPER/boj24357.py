# 백준 24357번 MINESWEEPER
import sys
put = sys.stdin.readline

data = [list(map(int, put().split())) for i in range(3)]

dx = [-1, -1, -1,  0, 0, 1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]

answer = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        if data[i][j] == 9:
            answer[i][j] = 9

        else:
            for d in range(8):
                x, y = i + dx[d], j + dy[d]
                if 0 <= x < 3 and 0 <= y < 3 and data[x][y] == 9:
                    answer[i][j] += 1

for i in answer:
    print(*i)
