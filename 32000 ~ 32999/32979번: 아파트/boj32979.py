# 백준 32979번 아파트
import sys
put = sys.stdin.readline

N = int(put())
T = int(put())
a = list(map(int, put().split()))
b = list(map(int, put().split()))

answer = []

for bi in b:
    i = (bi - 1) % len(a)
    a = a[i:] + a[:i]
    answer.append(a[0])

print(*answer)