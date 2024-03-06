# 백준 30803번 수도꼭지
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
a = [1] * N
cnt = sum(A)
print(cnt)

Q = int(put())
while Q:
    Q -= 1
    control = list(map(int, put().split()))

    if control[0] == 1:
        n, i, x = control
        if a[i-1]:
            cnt = cnt - A[i-1] + x
        A[i-1] = x
        print(cnt)

    else:
        n, i = control
        if a[i-1]:
            cnt -= A[i-1]
        else:
            cnt += A[i-1]

        a[i-1] ^= 1
        print(cnt)
