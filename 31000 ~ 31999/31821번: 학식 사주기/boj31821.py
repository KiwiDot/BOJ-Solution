# 백준 31821번 학식 사주기
import sys
put = sys.stdin.readline

N = int(put())
A = [0] + [int(put()) for i in range(N)]

M = int(put())
B = [A[int(put())] for i in range(M)]

print(sum(B))