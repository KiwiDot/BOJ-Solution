# 백준 32351번 리듬게임
import sys
put = sys.stdin.readline

N, S, K = put().split()
N, S, K = int(N), float(S), int(K)
answer = 0
n = 1

while K:
    K -= 1
    M, s = put().split()

    b = (int(M) - n) * 4
    answer += b * 60 / S

    n = int(M)
    S = float(s)

b = (N - n + 1) * 4
answer += b * 60 / S

print(f"{answer:.12f}")