# 백준 31614번 分 (Minutes)
import sys
put = sys.stdin.readline

H, M = [int(put()) for i in range(2)]
print(H * 60 + M)