# 백준 33573번 대칭제곱수
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = put().strip()

    n1 = round(int(N) ** 0.5)
    n2 = round(int(N[::-1]) ** 0.5)

    if n1 ** 2 == int(N) and n2 ** 2 == int(N[::-1]):
        print("YES")
    else:
        print("NO")