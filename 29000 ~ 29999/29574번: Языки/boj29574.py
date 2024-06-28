# 백준 29574번 Языки
import sys
put = sys.stdin.readline

num = put().split()
n = int(put())

while n:
    n -= 1
    a = [num[int(i)] for i in put().strip()]

    print(max(a))