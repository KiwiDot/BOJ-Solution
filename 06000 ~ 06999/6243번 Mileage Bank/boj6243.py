# 백준 6243번 Mileage Bank
import sys
from math import ceil
put = sys.stdin.readline

check = True
while check:
    mileage = 0
    while True:
        data = put().split()
        if data == ['#']:
            check = False
            break
        if data == ['0']:
            print(mileage)
            break

        s, d, m, c = data
        m = int(m)

        match c:
            case 'F':
                mileage += m * 2
            case 'B':
                mileage += ceil(m * 1.5)
            case 'Y':
                mileage += max(m, 500)

