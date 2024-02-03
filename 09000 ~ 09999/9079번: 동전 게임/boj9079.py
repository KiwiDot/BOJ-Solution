# 백준 9079번 동전 게임
import sys
from itertools import combinations
put = sys.stdin.readline
HT = {'H': 0, 'T': 1}

T = int(put())

while T:
    T -= 1
    coin = []
    for i in range(3):
        coin += [HT[j] for j in put().split()]

    r = [i for i in range(8)]
    answer = -1

    for i in range(9):
        for j in combinations(r, i):
            c = coin.copy()

            for k in j:
                if k == 0:
                    point = [0, 1, 2]
                elif k == 1:
                    point = [3, 4, 5]
                elif k == 2:
                    point = [6, 7, 8]
                elif k == 3:
                    point = [0, 3, 6]
                elif k == 4:
                    point = [1, 4, 7]
                elif k == 5:
                    point = [2, 5, 8]
                elif k == 6:
                    point = [0, 4, 8]
                else:
                    point = [2, 4, 6]

                for p in point:
                    c[p] ^= 1

            if c == [0] * 9 or c == [1] * 9:
                answer = i
                break

        if answer >= 0:
            break

    print(answer)