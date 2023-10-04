# 백준 30088번 공포의 면담실
import sys
put = sys.stdin.readline

N = int(put())
n = []

for i in range(N):
    t = list(map(int, put().split()))
    n.append(sum(t[1:]))

n.sort()
answer = 0
for i in range(N):
    answer += (N - i) * n[i]

print(answer)