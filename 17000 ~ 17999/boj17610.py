# 백준 17610번 양팔저울
import sys
put = sys.stdin.readline

k = int(put())
g = list(map(int, put().split()))

S = sum(g)
dp = {0}
n = 0

for i in g:
    new = set()
    for j in dp:
        new.add(i + j)
        new.add(abs(i - j))
    dp |= new

dp -= {0}
print(S - len(dp))