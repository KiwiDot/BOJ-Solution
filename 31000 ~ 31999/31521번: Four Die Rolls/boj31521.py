# 백준 31521번 Four Die Rolls
import sys
put = sys.stdin.readline

n = int(put())
dice = set(map(int, put().split()))

if len(dice) != n:
    Ashley = 0
else:
    Ashley = 1
    for i in range(4 - n):
        Ashley *= 6 - n - i

Brandon = 6 ** (4 - n) - Ashley
print(Ashley, Brandon)