# 백준 33557번 곱셈을 누가 이렇게 해 ㅋㅋ
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    A, B = put().split()

    size = max(len(A), len(B))
    a = A.rjust(size, '1')
    b = B.rjust(size, '1')

    AB = str(int(A) * int(B))
    ab = ''.join([str(int(a[i]) * int(b[i])) for i in range(size)])

    print(int(AB == ab))