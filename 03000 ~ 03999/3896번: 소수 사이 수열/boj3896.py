# 백준 3896번 소수 사이 수열
import sys
put = sys.stdin.readline

T = int(put())
prime = []
check = [1] * 1299710

for i in range(2, 1299710):
    if check[i]:
        prime.append(i)
        for j in range(i*2, 1299710, i):
            check[j] = 0

    else:
        check[i] = (prime[-1], len(prime))

while T:
    T -= 1
    k = int(put())
    if check[k] == 1:
        print(0)
    else:
        p, idx = check[k]
        print(prime[idx] - p)