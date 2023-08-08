# 백준 22973번 점프 숨바꼭질
import sys
put = sys.stdin.readline

K = int(put())
bin_k = bin(abs(K))[2:]
n = len(bin_k)

if K:
    for i in range(n, -1, -1):
        if K > 0:
            K -= 2 ** i
        else:
            K += 2 ** i

    print(-1 if K else n)

else:
    print(0)
