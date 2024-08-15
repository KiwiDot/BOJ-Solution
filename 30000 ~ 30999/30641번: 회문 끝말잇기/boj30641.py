# 백준 30641번 회문 끝말잇기
import sys
from math import ceil
put = sys.stdin.readline

L, U = map(int, put().split())
r = 10 ** 9 + 7
check = 0
n26 = [1]

for i in range(500000):
    n26.append(n26[-1] * 26 % r)

answer = 0
for i in range(L, U+1):
    if i <= 2:
        check ^= 1

    answer += n26[ceil((i-2)/2)]
    answer %= r

print('H' if check else 'A')
print(answer)