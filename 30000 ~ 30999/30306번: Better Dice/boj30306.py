# 백준 30306번 Better Dice
import sys
put = sys.stdin.readline

n = int(put())
d1 = sorted(list(map(int, put().split())))
d2 = sorted(list(map(int, put().split())))

cnt1 = cnt2 = 0
for i in range(n):
    for j in range(n):
        if d1[i] > d2[j]:
            cnt1 += 1
        elif d1[i] < d2[j]:
            cnt2 += 1

if cnt1 > cnt2:
    print("first")
elif cnt1 < cnt2:
    print("second")
else:
    print("tie")