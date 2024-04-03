# 백준 6796번 Punchy
import sys
put = sys.stdin.readline


def divide(X, Y):
    # 부호가 다른 나눗셈
    if X // abs(X) != Y // abs(Y):
        return -(abs(X) // abs(Y))
    return X // Y


X = {'A': 0, 'B': 0}

while True:
    text = put().split()

    match text[0]:
        case '1':
            X[text[1]] = int(text[2])
        case '2':
            print(X[text[1]])
        case '3':
            X[text[1]] += X[text[2]]
        case '4':
            X[text[1]] *= X[text[2]]
        case '5':
            X[text[1]] -= X[text[2]]
        case '6':
            X[text[1]] = divide(X[text[1]], X[text[2]])
        case '7':
            break