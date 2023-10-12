# 백준 29700번 우당탕탕 영화예매
import sys
put = sys.stdin.readline

N, M, K = map(int, put().split())
answer = 0

while N:
    N -= 1
    data = put().strip().split('1')
    for i in data:
        if len(i) >= K:
            answer += (len(i) - K + 1)

print(answer)