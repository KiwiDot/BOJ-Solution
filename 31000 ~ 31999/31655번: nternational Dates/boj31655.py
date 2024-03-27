# 백준 31655번 nternational Dates
import sys
put = sys.stdin.readline

A, B, C = map(int, put().strip().split('/'))

if 1 <= A <= 12 and 1 <= B <= 12:
    print("either")
elif 1 <= A <= 12:
    print("US")
else:
    print("EU")