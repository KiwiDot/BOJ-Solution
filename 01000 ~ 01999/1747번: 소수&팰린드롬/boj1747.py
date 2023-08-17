# 백준 1747번 소수&팰린드롬
import sys
put = sys.stdin.readline

answer = []
number = [1] * 2000000

for i in range(2, 2000000):
    if number[i]:
        if str(i) == str(i)[::-1]:
            answer.append(i)
        for j in range(i*2, 2000000, i):
            number[j] = 0

N = int(put())
for i in answer:
    if i >= N:
        print(i)
        break