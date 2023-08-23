# 백준 20922번 겹치는 건 싫어
import sys
from collections import deque
put = sys.stdin.readline

N, K = map(int, put().split())
a = list(map(int, put().split()))

answer = 0
queue = deque([])
cnt = dict([(i+1, 0) for i in range(100000)])

for i in a:
    while cnt[i] >= K:
        j = queue.popleft()
        cnt[j] -= 1

    queue.append(i)
    cnt[i] += 1

    answer = max(answer, len(queue))

print(answer)
