# 백준 29813번 최애의 팀원
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
queue = deque()

while N:
    N -= 1
    queue.append(put().split())

while len(queue) != 1:
    X = int(queue.popleft()[1])

    for i in range(X-1):
        queue.append(queue.popleft())

    queue.popleft()

answer = queue.popleft()[0]
print(answer)