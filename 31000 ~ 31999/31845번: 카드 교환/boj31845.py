# 백준 31845번 카드 교환
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = sorted(list(map(int, put().split())))
answer = 0

while M:
    M -= 1
    if A[-1] > 0:
        answer += A.pop()
        if A:
            A.pop(0)

    if not A:
        break

print(answer)