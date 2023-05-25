# 백준 2438번 별 찍기 - 1
import sys
put = sys.stdin.readline

N = int(put())
for i in range(N):
    print('*' * (i+1))
