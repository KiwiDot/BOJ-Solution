# 백준 7245번 Kurjeris
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
T = [0] * N
answer = [0] * N

while M:
    M -= 1
    z = list(map(int, put().split()))
    t, v = z.pop(0), z.pop(0)
    possible = []

    for i in range(N):
        if T[i] <= t:
            possible.append((i, z[i]))

    if possible:
        idx, min_z = min(possible, key=lambda x: x[1])
        T[idx] = t + min_z
        answer[idx] += v

print(*answer)