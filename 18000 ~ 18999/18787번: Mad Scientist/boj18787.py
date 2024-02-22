# 백준 18787번 Mad Scientist
import sys
put = sys.stdin.readline

N = int(put())
A = ' ' + put().strip()
B = ' ' + put().strip()
answer = 0

for i in range(1, N+1):
    if A[i-1] == B[i-1] and A[i] != B[i]:
        answer += 1

print(answer)