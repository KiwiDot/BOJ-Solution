# 백준 10164번 격자상의 경로
import sys
from math import factorial
put = sys.stdin.readline

N, M, K = map(int, put().split())

if K:
    k = K - 1
    n1, m1 = k // M, k % M
    n2, m2 = N - n1 - 1, M - m1 -1

    route1 = factorial(n1 + m1) // factorial(n1) // factorial(m1)
    route2 = factorial(n2 + m2) // factorial(n2) // factorial(m2)

    print(route1 * route2)

else:
    N -= 1
    M -= 1
    answer = factorial(N + M) // factorial(N) // factorial(M)
    print(answer)