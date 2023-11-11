# 백준 30596번 Axis-Aligned Area
import sys
put = sys.stdin.readline

a = sorted([int(put()) for i in range(4)])
answer = a[0] * a[2]

print(answer)