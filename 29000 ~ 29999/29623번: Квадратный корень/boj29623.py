# 백준 29623번 Квадратный корень
import sys
from decimal import Decimal
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    A, B, C, D = map(int, put().split())
    b = Decimal(str(B)) ** Decimal('0.5')
    d = Decimal(str(D)) ** Decimal('0.5')

    L = A + b
    R = C + d

    if L < R:
        print("Less")
    elif L == R:
        print("Equal")
    else:
        print("Greater")