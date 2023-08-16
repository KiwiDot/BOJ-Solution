# 백준 1850번 최대공약수
import sys
from math import gcd
put = sys.stdin.readline

A, B = map(int, put().split())

print('1' * gcd(A, B))