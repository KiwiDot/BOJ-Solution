# 백준 28279번 덱 2
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
dq = deque()

while N:
    N -= 1
    n = put().split()

    if n[0] == '1':
        dq.appendleft(n[1])
    elif n[0] == '2':
        dq.append(n[1])
    elif n[0] == '3':
        print(dq.popleft() if dq else -1)
    elif n[0] == '4':
        print(dq.pop() if dq else -1)
    elif n[0] == '5':
        print(len(dq))
    elif n[0] == '6':
        print(int(not dq))
    elif n[0] == '7':
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)