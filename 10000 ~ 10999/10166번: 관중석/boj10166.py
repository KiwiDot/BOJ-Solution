# 백준 10166번 관중석
import sys
from math import gcd
put = sys.stdin.readline

D1, D2 = map(int, put().split())
check = [[1] * 2001 for i in range(2001)]
answer = 0

for i in range(D1, D2 + 1):
    for j in range(1, i+1):
        g = gcd(i, j)

        if check[i//g][j//g]:
            check[i//g][j//g] = 0
            answer += 1

print(answer)