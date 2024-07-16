# 백준 32068번 보물 찾기
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    L, R, S = map(int, put().split())

    l = 2 * (S - L)
    r = 2 * (R - S) - 1

    print(min(l, r) + 1)