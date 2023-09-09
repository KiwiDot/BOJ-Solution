# 백준 5133번 Recipes
import sys
from math import gcd
put = sys.stdin.readline

K = int(put())

for x in range(1, K+1):
    print("Data Set {}:".format(x))
    I, C = map(int, put().split())

    while I:
        I -= 1
        w, data = put().split()
        w = int(w)
        n, d = map(int, data.split('/'))

        w *= C
        n *= C

        w += n // d
        n %= d

        if n:
            g = gcd(n, d)
            print("{} {}/{}".format(w, n//g, d//g))
        else:
            print(w)
    print()