# 백준 11278번 2-SAT - 2
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
f = [list(map(int, put().split())) for i in range(M)]

for n in range(2 ** N):
    x = [int(i) for i in bin(n)[2:].zfill(N)]

    for i, j in f:
        xi = x[i-1] if i > 0 else x[abs(i)-1] ^ 1
        xj = x[j-1] if j > 0 else x[abs(j)-1] ^ 1

        if xi or xj:
            continue
        else:
            break

    else:
        print(1)
        print(*x)
        break

else:
    print(0)