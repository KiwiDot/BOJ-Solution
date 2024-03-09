# 백준 31473번 하늘과 핑크
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
B = list(map(int, put().split()))

a = sum(A) 
b = sum(B)

print(b, a)