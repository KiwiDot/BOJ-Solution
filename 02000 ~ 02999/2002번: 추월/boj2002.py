# 백준 2002번 추월
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
A = deque([put().strip() for i in range(N)])
B = deque([put().strip() for i in range(N)])

check = set()

while B:
    b = B.popleft()

    while A[0] in check:
        A.popleft()

    if A[0] == b:
        A.popleft()
    else:
        check.add(b)

print(len(check))