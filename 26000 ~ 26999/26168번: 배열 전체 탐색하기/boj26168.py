# 백준 26168번 배열 전체 탐색하기
import sys
from bisect import bisect_left, bisect_right
put = sys.stdin.readline

n, m = map(int, put().split())
A = sorted(list(map(int, put().split())))

while m:
    m -= 1
    q = list(map(int, put().split()))

    if q[0] == 1:
        k = q[1]
        print(n - bisect_left(A, k))

    elif q[0] == 2:
        k = q[1]
        print(n - bisect_right(A, k))

    else:
        i, j = q[1:]
        ii = bisect_left(A, i)
        jj = bisect_right(A, j)
        print(jj - ii)