# 백준 30823번 건공문자열
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
S = put().strip()
answer = S[K-1:]

if (N - K) % 2:
    answer += S[:K-1]
else:
    answer += S[:K-1][::-1]

print(answer)