# 백준 31216번 슈퍼 소수
import sys
put = sys.stdin.readline

prime, super_prime = [], []
number = [1] * 10 ** 6 * 4
number[0] = number[1] = 0

for i in range(2, 10 ** 6 * 4):
    if number[i]:
        prime.append(i)
        for j in range(i * 2, 10 ** 6 * 4, i):
            number[j] = 0
        if number[len(prime)]:
            super_prime.append(i)
            number[len(prime)] = 0

T = int(put())

while T:
    T -= 1
    n = int(put())
    print(super_prime[n-1])