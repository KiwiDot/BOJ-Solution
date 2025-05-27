# 백준 33990번 3대 512
import sys
put = sys.stdin.readline

N = int(put())
answer = set()

while N:
    N -= 1
    A, B, C = map(int, put().split())

    if A + B + C >= 512:
        answer.add(A + B + C)

if answer:
    print(min(answer))
else:
    print(-1)