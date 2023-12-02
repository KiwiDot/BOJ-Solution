# 백준 29864번 Tenniseturniir
import sys
put = sys.stdin.readline

n = list(map(int, put().split()))
a = list(map(int, put().split()))

r1, r2, r3 = [], [], []

for i in n:
    cnt = a.count(i)
    if cnt:
        r1.append(i)
    if cnt >= 2:
        r2.append(i)
    if cnt == 3:
        r3.append(i)

print(*r3)
print(*r2)
print(*r1)