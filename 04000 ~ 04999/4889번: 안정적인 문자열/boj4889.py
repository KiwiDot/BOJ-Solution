# 백준 4889번 안정적인 문자열
import sys
from collections import deque
put = sys.stdin.readline
idx = 0

while True:
    s = put().strip()
    if set(s) == {'-'}:
        break

    idx += 1
    answer = 0
    stack = deque()

    for i in s:
        if i == '}':
            if stack:
                stack.pop()
            else:
                answer += 1
                stack.append('{')
        else:
            stack.append(i)

    answer += len(stack) // 2
    print("{}. {}".format(idx, answer))