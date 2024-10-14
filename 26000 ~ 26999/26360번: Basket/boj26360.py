# 백준 26360번 Basket
import sys
put = sys.stdin.readline

X = int(put())

n1 = int(put())
n2 = int(put())
answer = n1 * X

if n2 == 1:
    answer += sum([int(put()) for i in range(1 if n1 else X)])

print(answer)