# 백준 32401번 ANA는 회문이야
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()

A = [i for i in range(N) if S[i] == 'A']
answer = 0

for i in range(len(A)-1):
    if S[A[i]:A[i+1]+1].count('N') == 1:
        answer += 1

print(answer)