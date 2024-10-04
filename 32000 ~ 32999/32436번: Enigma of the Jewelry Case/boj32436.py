# 백준 32436번 Enigma of the Jewelry Case
import sys
put = sys.stdin.readline

N = int(put())
K = [list(map(int, put().split())) for i in range(N)]

for i in range(4):
    check = True

    for j in range(N):
        k1 = K[j]
        k2 = [K[n][j] for n in range(N)]
        if k1 != sorted(k1) or k2 != sorted(k2):
            check = False
            break

    if check:
        print(i)
        break
    K = [[K[i][j] for i in range(N)] for j in range(N)][::-1]
