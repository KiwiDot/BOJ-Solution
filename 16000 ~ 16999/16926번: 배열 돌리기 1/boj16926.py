# 백준 16926번 배열 돌리기 1
import sys
put = sys.stdin.readline

N, M, R = map(int, put().split())
A = [list(map(int, put().split())) for i in range(N)]
n = min(N, M) // 2
arr = []
loc = []

for i in range(n):
    x = y = i
    arr.append([A[x][y]])
    loc.append([(x, y)])
    for j in range(N-i*2-1):
        x += 1
        arr[-1].append(A[x][y])
        loc[-1].append((x, y))
    for j in range(M-i*2-1):
        y += 1
        arr[-1].append(A[x][y])
        loc[-1].append((x, y))
    for j in range(N-i*2-1):
        x -= 1
        arr[-1].append(A[x][y])
        loc[-1].append((x, y))
    for j in range(M-i*2-2):
        y -= 1
        arr[-1].append(A[x][y])
        loc[-1].append((x, y))

answer = [[0] * M for i in range(N)]
for i in range(n):
    r = R % len(arr[i])
    arr[i] = arr[i][-r:] + arr[i][:-r]

    for j in range(len(arr[i])):
        x, y = loc[i][j]
        answer[x][y] = arr[i][j]

for i in answer:
    print(*i)