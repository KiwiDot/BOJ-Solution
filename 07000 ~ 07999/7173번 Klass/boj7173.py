# 백준 7173번 Klass
import sys
put = sys.stdin.readline

M, N = map(int, put().split())
num = [list(map(int, list(put().strip()))) for i in range(M)]
answer = 0

for i in range(M):
    for j in range(N):
        n = num[i][j]
        check = []

        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < M and 0 <= y < N:
                check.append(num[x][y])

        d = sum(abs(n - k) for k in check) / len(check)
        answer += d

print(f"{answer:.4f}")
