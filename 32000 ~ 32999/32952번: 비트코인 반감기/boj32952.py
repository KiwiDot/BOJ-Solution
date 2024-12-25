# 백준 32952번 비트코인 반감기
import sys
put = sys.stdin.readline

R, K, M = map(int, put().split())

R = R >> (M // K)

print(R)