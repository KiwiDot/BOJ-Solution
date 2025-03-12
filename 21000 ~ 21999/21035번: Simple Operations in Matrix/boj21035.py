# 백준 21035번 Simple Operations in Matrix
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = [list(map(int, put().split())) for i in range(N)]

Q = int(put())
while Q:
    Q -= 1
    rc, k, val = put().split()
    k, val = int(k), int(val)

    match rc:
        case "row":
            for i in range(M):
                A[k-1][i] += val

        case "col":
            for i in range(N):
                A[i][k-1] += val

sum_ans = max_ans = 0
min_ans = 10 ** 9

for i in range(N):
    for j in range(M):
        sum_ans += A[i][j]
        min_ans = min(min_ans, A[i][j])
        max_ans = max(max_ans, A[i][j])

print(sum_ans, min_ans, max_ans)