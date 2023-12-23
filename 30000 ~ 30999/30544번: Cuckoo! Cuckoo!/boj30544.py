# 백준 30544번 Cuckoo! Cuckoo!
import sys
put = sys.stdin.readline

HH, MM = map(int, put().strip().split(':'))
N = int(put())

if MM in {15, 30, 45}:
    N -= 1
elif MM == 00:
    N -= HH

if N > 0:
    N -= 1
    if MM < 15:
        MM = 15
    elif MM < 30:
        MM = 30
    elif MM < 45:
        MM = 45
    else:
        MM = 0
        HH += 1
        N -= (HH - 1)

while N > 0:
    MM += 15

    if MM == 60:
        MM = 0
        HH += 1
        if HH > 12:
            HH = 1
        N -= HH
    else:
        N -= 1

print("{}:{}".format(str(HH).zfill(2), str(MM).zfill(2)))