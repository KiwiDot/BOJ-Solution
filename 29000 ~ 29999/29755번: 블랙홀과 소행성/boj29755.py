# 백준 29755번 블랙홀과 소행성
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
b = sorted(list(map(int, put().split())))

left = -10 ** 9
right = b[0]
idx = 0

B = {}
for i in range(-1000000, 1000001):
    if i == b[idx]:
        B[i] = i
        idx = min(idx + 1, N - 1)

        left = i
        right = b[idx]

    elif abs(left - i) <= abs(right - i):
        B[i] = left

    else:
        B[i] = right

P = set()
while M:
    M -= 1
    a, w = map(int, put().split())

    distance = abs(B[a] - a)
    P.add(distance * w)

print(max(P))