# 백준 29725번 체스 초보 브실이
import sys
put = sys.stdin.readline

score = {'.': 0, 'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9}
for i in list(score.keys()):
    score[i.lower()] = -score[i]

answer = 0

for i in range(8):
    data = put().strip()

    for j in data:
        answer += score[j]

print(answer)