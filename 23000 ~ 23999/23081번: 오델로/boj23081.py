# 백준 23081번 오델로
import sys
put = sys.stdin.readline

N = int(put())
data = [list(put().strip()) for i in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        if data[i][j] != '.':
            continue

        cnt = 0
        move = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]

        for xi, yj in move:
            x, y = i + xi, j + yj
            count = 0

            while 0 <= x < N and 0 <= y < N:
                if data[x][y] == 'W':
                    count += 1
                else:
                    if data[x][y] == 'B':
                        cnt += count
                    break

                x += xi
                y += yj

        if cnt:
            answer.append([cnt, i, j])

if answer:
    answer = min(answer, key=lambda x: [-x[0], x[1], x[2]])
    print(answer[2], answer[1])
    print(answer[0])
else:
    print("PASS")