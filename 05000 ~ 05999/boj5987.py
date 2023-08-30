# 백준 5987번 String Function Encoding
import sys
put = sys.stdin.readline

Z = int(put())

while Z:
    Z -= 1
    N, C, S = put().split()
    N, C = int(N), int(C)

    while C:
        C -= 1
        S = S[N:] + S

    print(S)