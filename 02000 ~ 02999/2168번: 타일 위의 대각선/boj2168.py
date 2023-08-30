# 백준 2168번 타일 위의 대각선
import sys
from math import gcd
put = sys.stdin.readline

x, y = map(int, put().split())
answer = x + y - gcd(x, y)

print(answer)