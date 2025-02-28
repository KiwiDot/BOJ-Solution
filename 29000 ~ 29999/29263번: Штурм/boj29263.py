# 백준 29263번 Штурм
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
a = [list(map(int, put().split())) for i in range(n)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

for i in range(n):
    for j in range(m):
        for dx, dy in d:
            if 0 <= i + dx < n and 0 <= j + dy < m:
                if a[i][j] <= a[i+dx][j+dy]:
                    check = False
                    break
        else:
            answer += 1

print(answer)
