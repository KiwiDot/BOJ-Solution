# 백준 32369번 양파 실험
import sys
put = sys.stdin.readline

N, A, B = map(int, put().split())
o1 = o2 = 1

while N:
    N -= 1
    o1 += A
    o2 += B

    o1, o2 = max(o1, o2), min(o1, o2)
    if o1 == o2:
        o2 -= 1

print(o1, o2)