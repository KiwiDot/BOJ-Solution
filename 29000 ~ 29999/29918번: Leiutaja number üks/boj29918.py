# 백준 29918번 Leiutaja number üks
import sys
put = sys.stdin.readline

data = []
for i in range(6):
    N, M = map(int, put().split())
    data.append(N + M * 10)

Adalbert = data.pop(0)
if Adalbert > max(data):
    print(0)
else:
    print(max(data) - Adalbert + 1)