# 백준 31048번 Last Factorial Digit
import sys
from math import factorial
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())

    print(factorial(N) % 10)