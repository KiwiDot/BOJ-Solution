# 백준 7241번 Skaičiai
import sys
put = sys.stdin.readline

a, b, c = put().split()
x = put().strip()

answer = sorted([a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a]).index(x) + 1
print(answer)
