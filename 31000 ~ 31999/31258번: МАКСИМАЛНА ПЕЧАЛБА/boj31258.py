# 백준 31258번 МАКСИМАЛНА ПЕЧАЛБА
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
a = sorted(list(map(int, put().split())), reverse=True)
b = sorted(list(map(int, put().split())), reverse=True)

nm = min(n, m)
answer = 0

for i in range(nm):
    answer += a[i] * b[i]

print(nm, answer)