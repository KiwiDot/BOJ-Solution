# 백준 2531번 회전 초밥
import sys
from collections import deque
put = sys.stdin.readline

N, d, k, c = map(int, put().split())
sushi = [int(put()) for i in range(N)] * 2
event = deque(sushi[:k])
answer = len(set(event) | {c})

for i in range(k, N+k-1):
    event.popleft()
    event.append(sushi[i])
    answer = max(answer, len(set(event) | {c}))

print(answer)