# 백준 33675번 L-트로미노 타일링
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())

    if N % 2:
        print(0)

    else:
        print(2 ** (N // 2))