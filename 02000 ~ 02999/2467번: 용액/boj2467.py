# 백준 2467번 용액
import sys
put = sys.stdin.readline

N = int(put())
n = list(map(int, put().split()))

check = 10 ** 10
a = b = 0
i, j = 0, N-1

while i < j:
    c = abs(n[i] + n[j])
    if c < check:
        check = c
        a = n[i]
        b = n[j]

    if abs(n[i]) > abs(n[j]):
        i += 1
    elif abs(n[i]) < abs(n[j]):
        j -= 1
    else:
        break

print(a, b)