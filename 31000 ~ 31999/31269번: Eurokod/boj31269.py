# 백준 31269번 Eurokod
import sys
put = sys.stdin.readline

n = int(put())

a = list(map(int, put().split()))
b = list(map(int, put().split()))
b = sorted([[b[i], i+1] for i in range(n)], reverse=True)

score = [[i, 0, 0] for i in range(n+1)]

for i in range(n):
    score[a[i]][1] += n - i
    score[b[i][1]][2] += n - i

score.pop(0)
score.sort(key=lambda x: [-(x[1] + x[2]), -x[2]])

for i in range(n):
    rank = i + 1
    label = str(score[i][0]).zfill(2)
    points = score[i][1] + score[i][2]

    print(f"{rank}. Kod{label} ({points})")
