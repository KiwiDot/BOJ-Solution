# 백준 31870번 버블버블
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
a = A.copy()

answer1 = 0
for i in range(N-1, -1, -1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            answer1 += 1
            a[j], a[j+1] = a[j+1], a[j]

answer2 = 1
for i in range(N):
    for j in range(N-1, i, -1):
        if A[j] > A[j-1]:
            answer2 += 1
            A[j], A[j-1] = A[j-1], A[j]

print(min(answer1, answer2))