# 백준 32385번 1_2(MatKor+ALPS)=AlKor
import sys
put = sys.stdin.readline

N = n = int(put())
x = 10 ** 9
A = []

while n > 2:
    n -= 2
    A.extend([x, -x])
    x -= 1

if n == 1:
    A.extend([N, 1])
else:
    A.extend([x, N-x, 1])

print(*A)