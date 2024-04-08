# 백준 31738번 매우 어려운 문제
import sys
put = sys.stdin.readline

N, M = map(int, put().split())

if N >= M or N >= M * 2:
    print(0)

else:
    answer = 1
    for i in range(1, N+1):
        answer = (answer * i) % M

    print(answer)