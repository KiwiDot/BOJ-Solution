# 백준 2824번 최대공약수
import sys
from collections import defaultdict
put = sys.stdin.readline

N = int(put())
n = list(map(int, put().split()))

M = int(put())
m = list(map(int, put().split()))

A, B = defaultdict(int), defaultdict(int)

# 2 ~ 40000까지의 소수
prime = []
num = [1] * 40000
for i in range(2, 40000):
    if num[i]:
        prime.append(i)

        for j in range(i, 40000, i):
            num[j] = 0

for a in n:
    for i in prime:
        if i > a:
            break

        while a % i == 0:
            a //= i
            A[i] += 1

    if a:
        A[a] += 1

for b in m:
    for i in prime:
        if i > b:
            break

        while b % i == 0:
            b //= i
            B[i] += 1

    if b:
        B[b] += 1

answer = 1
for i in set(A.keys()) & set(B.keys()):
    answer *= i ** min(A[i], B[i])
    answer %= 10 ** 12

print(str(answer)[-9:])