# 백준 29758번 제곱근 수열
import sys
put = sys.stdin.readline


def solution(n, l):
    global answer
    if n == l == 1:
        answer += 1
    else:
        for i in range(1, A[n]+1):
            solution(i, l - 1)


A = {}
for i in range(70001):
    A[i] = int(i ** 0.5 - 0.1 ** 10)

T = int(put())

while T:
    T -= 1
    N, L = map(int, put().split())
    answer = 0

    solution(N, L)
    print(answer)