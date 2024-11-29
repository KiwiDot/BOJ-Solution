# 백준 32801번 Generalized FizzBuzz
import sys
from math import lcm
put = sys.stdin.readline

n, a, b = map(int, put().split())
lc = lcm(a, b)

FizzBuzz = n // lc
Fizz = n // a - FizzBuzz
Buzz = n // b - FizzBuzz

print(Fizz, Buzz, FizzBuzz)