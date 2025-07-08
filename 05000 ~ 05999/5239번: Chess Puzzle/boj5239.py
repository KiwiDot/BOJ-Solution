# 백준 5239번 Chess Puzzle
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    data = list(map(int, put().split()))
    n = data[0]

    x = []
    y = []

    for i in range(data[0]):
        x.append(data[i * 2 + 1])
        y.append(data[i * 2 + 2])

    check = True

    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                check = False
                break
        else:
            continue

        break

    if check:
        print("SAFE")
    else:
        print("NOT SAFE")
