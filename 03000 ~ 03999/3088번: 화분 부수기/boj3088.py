# 백준 3088번 화분 부수기
import sys
put = sys.stdin.readline

N = int(put())
data = [set(put().split()) for i in range(N)]

answer = 1
for i in range(1, N):
    if not data[0] & data[i]:
        answer += 1
    data[0] |= data[i]

print(answer)