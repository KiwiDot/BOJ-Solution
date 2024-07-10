# 백준 3432번 Game
import sys
put = sys.stdin.readline

Z = int(put())

while Z:
    Z -= 1
    data = [list(put().strip()) for i in range(5)]
    check = set()

    for i in data:
        check.add(''.join(i))

    for i in range(5):
        check.add(''.join(data[j][i] for j in range(5)))

    for i in range(5):
        for j in range(5):
            if i <= 2 and j <= 2:
                check.add(''.join(data[i+k][j+k] for k in range(3)))
            if i <= 2 <= j:
                check.add(''.join(data[i+k][j-k] for k in range(3)))

    answer = 0
    if any("AAA" in i for i in check):
        answer += 1
    if any("BBB" in i for i in check):
        answer -= 1

    match answer:
        case 1:
            print("A wins")
        case -1:
            print("B wins")
        case 0:
            print("draw")