# 백준 28356번 부정행위 멈춰!
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
i0 = [1, 2] * 1000
i1 = [3, 4] * 1000

if N == M == 1:
    print(1)
    print(1)

elif N == 1 or M == 1:
    print(2)
    for i in range(N):
        print(*[i0[(i + j) % 2] for j in range(M)])

else:
    print(4)

    for i in range(N):
        if i % 2:
            print(*i0[:M])
        else:
            print(*i1[:M])