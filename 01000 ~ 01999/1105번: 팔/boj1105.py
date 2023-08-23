# 백준 1105번 팔
import sys
put = sys.stdin.readline

L, R = put().split()
n = max(len(L), len(R))
L = L.zfill(n)
R = R.zfill(n)

answer = 0
for i in range(n):
    if L[i] == R[i]:
        if L[i] == '8':
            answer += 1
    else:
        break

print(answer)