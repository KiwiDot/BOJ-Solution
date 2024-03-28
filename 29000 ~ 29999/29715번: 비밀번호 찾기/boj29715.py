# 백준 29715번 비밀번호 찾기
import sys
from math import factorial
put = sys.stdin.readline

N, M = map(int, put().split())
X, Y = map(int, put().split())
password = ["-"] * N
possible = set()

while M:
    M -= 1
    a, b = map(int, put().split())
    if a:
        password[a-1] = b
    else:
        possible.add(b)

possible -= set(password)
num = {i for i in range(1, 10)} - possible - set(password)
n = password.count("-")
r = n - len(possible)

cnt = factorial(n) * factorial(len(num)) // factorial(r) // factorial(len(num) - r)
c3 = (cnt - 1) // 3 if cnt else 0

print(cnt * X + c3 * Y)