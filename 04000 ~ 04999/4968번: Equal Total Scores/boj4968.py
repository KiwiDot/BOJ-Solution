# 백준 4968번 Equal Total Scores
import sys
put = sys.stdin.readline

while True:
    n, m = map(int, put().split())
    if n == m == 0:
        break
    Taro = sorted([int(put()) for i in range(n)])
    Hanako = sorted([int(put()) for i in range(m)])

    if sum(Taro) > sum(Hanako):
        diff = sum(Taro) - sum(Hanako)
        if diff % 2:
            print(-1)
        else:
            diff //= 2
            for i in Hanako:
                if i + diff in Taro:
                    print(i+diff, i)
                    break
            else:
                print(-1)

    else:
        diff = sum(Hanako) - sum(Taro)
        if diff % 2:
            print(-1)
        else:
            diff //= 2
            for i in Taro:
                if i + diff in Hanako:
                    print(i, i+diff)
                    break
            else:
                print(-1)