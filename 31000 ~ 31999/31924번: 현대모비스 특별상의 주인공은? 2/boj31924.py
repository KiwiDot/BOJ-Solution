# 백준 31924번 현대모비스 특별상의 주인공은? 2
import sys
put = sys.stdin.readline

N = int(put())
data = ['*' * (N + 8)] * 4 + ['*' * 4 + put().strip() + '*' * 4 for i in range(N)] + ['*' * (N + 8)] * 4
answer = 0

for i in range(4, N+4):
    for j in range(4, N+4):
        for ii, jj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            d = [data[i + ii * k][j + jj * k] for k in range(5)]
            if d == list("MOBIS"):
                answer += 1

print(answer)
