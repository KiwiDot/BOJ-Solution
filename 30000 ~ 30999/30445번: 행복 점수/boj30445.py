# 백준 30445번 행복 점수
import sys
put = sys.stdin.readline

HAPPY = {'H', 'A', 'P', 'Y'}
SAD = {'S', 'A', 'D'}

PH = PG = 0
msg = put().strip()

for i in msg:
    if i in HAPPY:
        PH += 1
    if i in SAD:
        PG += 1

if PH == PG == 0:
    print("50.00")
else:
    H = PH * 10000 / (PH + PG)
    H = int(H + 0.5) / 100
    print("{:.2f}".format(H))