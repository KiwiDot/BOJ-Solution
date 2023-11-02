# 백준 28298번 더 흔한 타일 색칠 문제
import sys
put = sys.stdin.readline

N, M, K = map(int, put().split())
d = [list(put().strip()) for i in range(N)]
k = [[{} for j in range(K)] for i in range(K)]
n = N // K
m = M // K

for i in range(0, N, K):
    for j in range(0, M, K):
        for ki in range(K):
            for kj in range(K):
                if d[i+ki][j+kj] in k[ki][kj]:
                    k[ki][kj][d[i+ki][j+kj]] += 1
                else:
                    k[ki][kj][d[i+ki][j+kj]] = 1

answer = 0
for ki in range(K):
    for kj in range(K):
        kij = max(k[ki][kj], key=lambda x: k[ki][kj][x])
        answer += n * m - k[ki][kj][kij]
        k[ki][kj] = kij

print(answer)
for i in range(n):
    for j in k:
        print(''.join(j) * m)