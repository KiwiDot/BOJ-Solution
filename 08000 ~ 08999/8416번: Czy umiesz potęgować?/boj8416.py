# 백준 8416번 Czy umiesz potęgować?
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
b -= 1
num = [a % 10]

while True:
    ai = (num[-1] * a) % 10
    if ai in num:
        break
    num.append(ai)

idx = b % len(num)
print(num[idx])