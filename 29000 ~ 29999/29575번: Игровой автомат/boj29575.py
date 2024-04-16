# 백준 29575번 Игровой автомат
import sys
put = sys.stdin.readline

n = int(put())
check = {}

while n:
    n -= 1
    c, w = put().split()
    check[c] = int(w)

m = int(put())
answer = 0

while m:
    m -= 1
    answer -= 10
    c = put().strip()

    if c in check:
        answer += check[c]

print(answer)