# 백준 26577번 Math
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    text = put().strip().replace('/', '//')

    print(eval(text))