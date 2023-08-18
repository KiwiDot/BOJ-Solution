# 백준 29220번 Свидание
import sys
put = sys.stdin.readline

k = int(put())
n = int(put())
a = sorted(list(map(int, put().split())))

if sum(a[1:]) >= k:
    print("YES")
else:
    print("NO")
