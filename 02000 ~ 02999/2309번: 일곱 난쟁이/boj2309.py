# 백준 2309번 일곱 난쟁이
import sys
put = sys.stdin.readline

k = sorted([int(put()) for i in range(9)])
K = sum(k)
answer = []

for i in range(9):
    for j in range(i+1, 9):
        if K - k[i] - k[j] == 100:
            answer = k[:i] + k[i+1:j] + k[j+1:]

for i in answer:
    print(i)