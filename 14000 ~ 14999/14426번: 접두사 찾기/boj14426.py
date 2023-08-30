# 백준 14426번 접두사 찾기
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
S = sorted([put().strip() for i in range(N)])
s = sorted([put().strip() for i in range(M)])
idx = 0

answer = 0
for i in s:
    while idx < N - 1 and S[idx] < i:
        idx += 1

    if S[idx].startswith(i):
        answer += 1

print(answer)