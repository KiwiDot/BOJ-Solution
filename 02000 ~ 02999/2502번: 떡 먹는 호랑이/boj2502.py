# 백준 2502번 떡 먹는 호랑이
import sys
put = sys.stdin.readline

D, K = map(int, put().split())
ab = [(1, 0), (0, 1)]

for i in range(2, 30):
    ab.append((ab[i-2][0] + ab[i-1][0], ab[i-2][1] + ab[i-1][1]))

a, b = ab[D-1]
for A in range(1, K // a + 1):
    B = (K - a * A) // b

    if A <= B and a * A + b * B == K:
        print(A)
        print(B)
        break