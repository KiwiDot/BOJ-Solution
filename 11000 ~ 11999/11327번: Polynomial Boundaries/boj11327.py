# 백준 11327번 Polynomial Boundaries
import sys
put = sys.stdin.readline

while True:
    data = put().split()
    if data == ['0']:
        break

    N = int(data.pop(0))
    a = list(map(int, data))
    x, y = list(map(int, put().split()))

    ax = 0
    for i in range(N):
        ax += x ** i * a[i]

    if ax > y:
        print("Inside")
    elif ax < y:
        print("Outside")
    else:
        print("On")