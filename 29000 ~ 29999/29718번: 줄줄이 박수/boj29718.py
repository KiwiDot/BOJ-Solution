# 백준 29718번 줄줄이 박수
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
Q = [0] * M

while N:
    N -= 1
    Qi = list(map(int, put().split()))

    for i in range(M):
        Q[i] += Qi[i]

A = int(put())
a = sum(Q[:A])

answer = [a]
for i in range(A, M):
    a = a + Q[i] - Q[i-A]
    answer.append(a)

print(max(answer))