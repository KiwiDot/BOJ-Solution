# 백준 32279번 수열의 비밀 (Easy)
import sys
put = sys.stdin.readline

n = int(put())
p, q, r, s = map(int, put().split())
a = [0, int(put())]

for i in range(2, n+1):
    if i % 2:
        a.append(r * a[(i-1) // 2] + s)
    else:
        a.append(p * a[i//2] + q)

print(sum(a))