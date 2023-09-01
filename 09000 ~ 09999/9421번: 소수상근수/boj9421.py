# 백준 9421번 소수상근수
import sys
put = sys.stdin.readline

n = int(put())
prime = []
check = [1] * (n+1)

for i in range(2, n+1):
    if check[i]:
        prime.append(i)
        for j in range(i*2, n+1, i):
            check[j] = 0

for i in prime:
    n = i
    num = set()
    while n not in num:
        num.add(n)
        n = sum([int(j) ** 2 for j in str(n)])

    if n == 1:
        print(i)