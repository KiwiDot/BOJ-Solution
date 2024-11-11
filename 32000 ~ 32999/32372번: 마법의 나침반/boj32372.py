# 백준 32372번 마법의 나침반
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
x, y = set([i+1 for i in range(N)]), set([i+1 for i in range(N)])

while M:
    M -= 1
    X, Y, K = map(int, put().split())

    match K:
        case 1:
            x -= {i for i in range(X, N+1)}
            y = {Y}

        case 2:
            x -= {i for i in range(X, N+1)}
            y -= {i for i in range(1, Y+1)}

        case 3:
            x = {X}
            y -= {i for i in range(1, Y+1)}

        case 4:
            x -= {i for i in range(1, X+1)}
            y -= {i for i in range(1, Y+1)}

        case 5:
            x -= {i for i in range(1, X+1)}
            y = {Y}

        case 6:
            x -= {i for i in range(1, X+1)}
            y -= {i for i in range(Y, N+1)}

        case 7:
            x = {X}
            y -= {i for i in range(Y, N+1)}

        case 8:
            x -= {i for i in range(X, N+1)}
            y -= {i for i in range(Y, N+1)}

print(list(x)[0], list(y)[0])
