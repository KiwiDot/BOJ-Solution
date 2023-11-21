# 백준 30619번 내 집 마련하기
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

M = int(put())
while M:
    M -= 1
    L, R = map(int, put().split())
    a = []
    idx = []

    for i in range(N):
        if L <= A[i] <= R:
            a.append(A[i])
            idx.append(i)

    answer = A.copy()
    a.sort()
    for i in range(len(a)):
        answer[idx[i]] = a[i]

    print(*answer)