# 백준 1051번 숫자 정사각형
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = [put().strip() for i in range(N)]
answer = 1

for i in range(N):
    for j in range(M):
        for k in range(min(N-i, M-j)):
            if data[i][j] == data[i+k][j] == data[i][j+k] == data[i+k][j+k]:
                answer = max(answer, (k+1) ** 2)

print(answer)