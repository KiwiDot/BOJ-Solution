# 백준 30456번 바닥수
import sys
put = sys.stdin.readline

N, L = map(int, put().split())
print('1' * (L - 1) + str(N))