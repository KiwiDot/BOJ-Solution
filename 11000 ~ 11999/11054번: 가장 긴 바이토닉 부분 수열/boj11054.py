# 백준 11054번 가장 긴 바이토닉 부분 수열
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

S1_K = []
SK_N = []

for i in range(N):
    check = {1}
    for a, cnt, idx in S1_K:
        if a < A[i]:
            check.add(cnt + 1)

    S1_K.append((A[i], max(check), i))

    check = {0}
    for a, cnt, idx in SK_N:
        if a < A[N-i-1]:
            check.add(cnt + 1)
    SK_N.append((A[N-i-1], max(check), N-i-1))

SK_N = SK_N[::-1]
answer = 0

for i in range(N):
    cnt = S1_K[i][1] + SK_N[i][1]
    answer = max(answer, cnt)

print(answer)