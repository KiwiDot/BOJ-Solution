# 백준 32432번 Attention to the Meeting
import sys
put = sys.stdin.readline

N = int(put())
K = int(put()) - (N - 1)

print(K // N)