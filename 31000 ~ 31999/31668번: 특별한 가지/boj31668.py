# 백준 31668번 특별한 가지
import sys
put = sys.stdin.readline

N, M, K = [int(put()) for i in range(3)]

print(M // N * K)