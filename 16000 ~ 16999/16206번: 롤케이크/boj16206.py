# 백준 16206번 롤케이크
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = sorted(list(map(int, put().split())), key=lambda x: [x % 10, x])
answer = 0

for i in range(N):
    if A[i] == 10:
        answer += 1

    elif A[i] % 10 == 0:
        a = min(M, A[i] // 10 - 1)
        answer += a
        if a == A[i] // 10 - 1:
            answer += 1
        M -= a

    else:
        a = min(M, A[i] // 10)
        answer += a
        M -= a

    if not M:
        break

print(answer)