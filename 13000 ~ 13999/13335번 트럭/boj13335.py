# 백준 13335번 트럭
import sys
from collections import deque
put = sys.stdin.readline

n, w, L = map(int, put().split())
a = deque(map(int, put().split()))
bridge = deque([0] * w)
answer = weight = 0

while a:
    answer += 1
    weight -= bridge.popleft()

    if weight + a[0] <= L:
        bridge.append(a[0])
        weight += a.popleft()
    else:
        bridge.append(0)

while weight:
    answer += 1
    weight -= bridge.popleft()

print(answer)