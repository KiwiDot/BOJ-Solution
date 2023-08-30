# 백준 20364번 부동산 다툼
import sys
put = sys.stdin.readline

N, Q = map(int, put().split())
owned = [0] * (N + 1)

while Q:
    Q -= 1
    X = x = int(put())
    answer = 0

    while x > 1:
        if owned[x]:
            answer = x
        x //= 2

    if answer == 0:
        owned[X] = 1
    print(answer)