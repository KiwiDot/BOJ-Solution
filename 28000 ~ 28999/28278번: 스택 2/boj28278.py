# 백준 28278번 스택 2
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
stack = deque()

while N:
    N -= 1
    n = put().split()

    if n[0] == '1':
        stack.appendleft(n[1])
    elif n[0] == '2':
        print(stack.popleft() if stack else -1)
    elif n[0] == '3':
        print(len(stack))
    elif n[0] == '4':
        print(0 if stack else 1)
    else:
        print(stack[0] if stack else -1)