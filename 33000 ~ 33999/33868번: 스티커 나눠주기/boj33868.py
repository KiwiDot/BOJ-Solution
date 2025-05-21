# 백준 33868번 스티커 나눠주기
import sys
put = sys.stdin.readline

N = int(put())
t = 0
b = 10 ** 9

while N:
    N -= 1
    T, B = map(int, put().split())
    t = max(t, T)
    b = min(b, B)

print(t * b % 7 + 1)