# 백준 32749번 타노수
import sys
put = sys.stdin.readline

N, T = map(int, put().split())
t = 2 ** (N - T)
X = put().strip()

answer = max([X[i:i+t] for i in range(0, 2 ** N, t)])
print(answer)