# 백준 2667번 단지번호붙이기
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
data = [list(put().strip()) for i in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        if data[i][j] == '0':
            continue

        cnt = 1
        data[i][j] = '0'
        visit = deque([(i, j)])

        while visit:
            x, y = visit.popleft()
            for xi, yi in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= xi < N and 0 <= yi < N and data[xi][yi] == '1':
                    data[xi][yi] = '0'
                    cnt += 1
                    visit.append((xi, yi))

        answer.append(cnt)

print(len(answer))
for i in sorted(answer):
    print(i)