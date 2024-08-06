# 백준 31872번 강의실
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
A = [0] + sorted(list(map(int, put().split())))

d = sorted([A[i+1] - A[i] for i in range(N)], reverse=True)

print(sum(d[K:]))

