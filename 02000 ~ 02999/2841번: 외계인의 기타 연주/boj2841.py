# 백준 2841번 외계인의 기타 연주
import sys
from collections import deque
put = sys.stdin.readline

N, P = map(int, put().split())
guitar = [deque() for i in range(7)]
answer = 0

while N:
    N -= 1
    n, p = map(int, put().split())

    while guitar[n] and guitar[n][-1] > p:
        guitar[n].pop()
        answer += 1

    if guitar[n] and guitar[n][-1] == p:
        continue
    else:
        guitar[n].append(p)
        answer += 1

print(answer)