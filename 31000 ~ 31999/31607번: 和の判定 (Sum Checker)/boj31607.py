# 백준 31607번 和の判定 (Sum Checker)
import sys
put = sys.stdin.readline

ABC = [int(put()) for i in range(3)]

if sum(ABC) / 2 in ABC:
    print(1)
else:
    print(0)