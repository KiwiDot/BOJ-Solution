# 백준 28110번 마지막 문제
import sys
put = sys.stdin.readline

N = int(put())
A = sorted(list(map(int, put().split())))

check = 0
answer = -1
for i in range(1, N):
    c = (A[i] - A[i-1]) // 2
    if c > check:
        answer = A[i-1] + c
        check = c
print(answer)
