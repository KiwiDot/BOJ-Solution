# 백준 30143번 Cookie Piles
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N, A, D = map(int, put().split())
    a1, an = A, A + (N - 1) * D

    answer = ((a1 + an) * N) // 2
    print(answer)
