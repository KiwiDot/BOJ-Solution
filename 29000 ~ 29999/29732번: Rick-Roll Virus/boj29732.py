# 백준 29732번 Rick-Roll Virus
import sys
put = sys.stdin.readline

N, M, K = map(int, put().split())
S = list(put().strip())

s = S.copy()
for i in range(N):
    if S[i] == 'R':
        for k in range(1, K+1):
            s[max(0, i-k)] = 'R'
            s[min(N-1, i+k)] = 'R'

m = s.count('R')
print("Yes" if m <= M else "No")