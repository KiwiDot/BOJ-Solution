# 백준 31052번 Relocation
import sys
put = sys.stdin.readline

N, Q = map(int, put().split())
x = list(map(int, put().split()))

while Q:
    Q -= 1
    n = list(map(int, put().split()))

    match n[0]:
        case 1:
            C, X = n[1:]
            x[C-1] = X
        case 2:
            A, B = n[1:]
            print(abs(x[A-1] - x[B-1]))