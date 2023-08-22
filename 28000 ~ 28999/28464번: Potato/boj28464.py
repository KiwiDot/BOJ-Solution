# 백준 28464번 Potato
import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
a = deque(sorted(list(map(int, put().split()))))

answer1 = 0
answer2 = 0

while a:
    answer1 += a.pop()
    if a:
        answer2 += a.popleft()

print(answer2, answer1)