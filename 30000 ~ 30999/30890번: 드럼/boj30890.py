# 백준 30890번 드럼
import sys
from math import lcm
put = sys.stdin.readline

X, Y = map(int, put().split())
l = lcm(X, Y)
x, y = l // X, l // Y
answer = ""

for i in range(1, l+1):
    if i % x == i % y == 0:
        answer += "3"
    elif i % x == 0:
        answer += "1"
    elif i % y == 0:
        answer += "2"

print(answer)