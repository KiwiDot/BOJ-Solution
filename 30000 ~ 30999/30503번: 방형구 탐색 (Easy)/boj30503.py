# 백준 30503번 방형구 탐색 (Easy)
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

Q = int(put())
while Q:
    Q -= 1
    query = put().split()

    if query[0] == '1':
        l, r, k = map(int, query[1:])
        print(A[l-1:r].count(k))

    else:
        l, r = map(int, query[1:])
        for i in range(l-1, r):
            A[i] = 0

