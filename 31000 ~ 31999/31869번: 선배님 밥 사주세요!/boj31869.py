# 백준 31869번 선배님 밥 사주세요!
import sys
put = sys.stdin.readline

N = int(put())
data = {}

for i in range(N):
    S, W, D, P = put().split()
    data[S] = (int(P), int(W) * 7 + int(D))

check = [' '] * 100
for i in range(N):
    S, M = put().split()
    m = data[S][0]

    if m <= int(M):
        check[data[S][1]] = '*'

answer = {0}
for i in ''.join(check).split():
    answer.add(len(i))

print(max(answer))