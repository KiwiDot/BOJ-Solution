# 백준 28419번 더하기
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
a = [0, 0]

for i in range(N):
    a[i % 2] += A[i]

print(abs(a[0] - a[1]) if N > 3 or a[0] <= a[1] else -1)