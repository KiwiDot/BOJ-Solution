# 백준 16564번 히오스 프로게이머
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
X = [int(put()) for i in range(N)]

start, end = min(X), max(X) + K
answer = 0

while start <= end:
    mid = (start + end) // 2
    k = sum([mid - x for x in X if mid > x])

    if k <= K:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)