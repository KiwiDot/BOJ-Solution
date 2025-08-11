# 백준 11264번 Logical Functions: AND-OR
import sys
put = sys.stdin.readline

truth_table = {"AND": [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)],
               "OR": [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]}

T = int(put())

while T:
    T -= 1
    data = put().split()
    logic = data.pop(0)

    W1, W2, B = map(float, data)

    for X1, X2, A in truth_table[logic]:
        a = int(W1*X1 + W2*X2 + B >= 0)
        if a != A:
            print("false")
            break
    else:
        print("true")
