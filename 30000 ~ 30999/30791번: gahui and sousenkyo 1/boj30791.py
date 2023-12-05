# 백준 30791번 gahui and sousenkyo 1
import sys
put = sys.stdin.readline

rank = list(map(int, put().split()))
rank16 = max(rank)
answer = 0

for i in rank:
    if i != rank16 and rank16 - i <= 1000:
        answer += 1

print(answer)