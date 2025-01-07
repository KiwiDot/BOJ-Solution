# 백준 31244번 СИМЕТРИЧНИ ЧИСЛА
import sys
put = sys.stdin.readline

A, B, C = put().split()

if A == C:
    print(A + B + C)

elif B == C:
    print(A + B + C + A)

else:
    print(A + B + C + B + A)