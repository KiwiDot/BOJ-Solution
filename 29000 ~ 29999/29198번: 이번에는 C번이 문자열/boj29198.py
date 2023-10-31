# 백준 29198번 이번에는 C번이 문자열
import sys
put = sys.stdin.readline

N, M, K = map(int, put().split())
S = sorted([''.join(sorted(list(put().strip()))) for i in range(N)])

answer = ""
for i in range(K):
    answer += S[i]

print(''.join(sorted(list(answer))))