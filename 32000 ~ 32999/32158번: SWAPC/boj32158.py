# 백준 32158번 SWAPC
import sys
put = sys.stdin.readline

n = int(put())
S = list(put().strip())

P = []
C = []

for i in range(n):
    if S[i] == 'P':
        P.append(i)
    if S[i] == 'C':
        C.append(i)

for i in range(min(len(P), len(C))):
    p, c = P[i], C[i]
    S[p], S[c] = S[c], S[p]

print(''.join(S))