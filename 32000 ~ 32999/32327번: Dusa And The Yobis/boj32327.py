# 백준 32327번 Dusa And The Yobis
D = int(input())

while True:
    try:
        Y = int(input())
        if D > Y:
            D += Y
        else:
            break

    except EOFError:
        break

print(D)