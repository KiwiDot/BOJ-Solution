# 백준 2739번 구구단
import sys
put = sys.stdin.readline

N = int(put())

for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N*i))
