# 백준 32316번 Ready for Contest
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
problem = [set() for i in range(n+1)]

while m:
    m -= 1
    p, L = map(int, put().split())
    problem[p].add(L)

for i in range(n+1):
    if 1 in problem[i] and 2 in problem[i]:
        print(i)