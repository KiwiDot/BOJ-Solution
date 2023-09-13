# 백준 29735번 택배가 안와잉
import sys
from math import ceil
put = sys.stdin.readline

t1, t2 = put().split()
N, T = map(int, put().split())

H1, M1 = map(int, t1.split(':'))
H2, M2 = map(int, t2.split(':'))

t = (H2 - H1) * 60 + (M2 - M1)
n = ceil(t / T) - 1

day, N = divmod(N, n)

t = H1 * 60 + M1 + T * (N + 1)
H, M = divmod(t, 60)

print(day)
print(str(H).zfill(2) + ':' + str(M).zfill(2))