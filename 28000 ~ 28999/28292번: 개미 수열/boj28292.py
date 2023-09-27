# 백준 28292번 개미 수열
import sys
put = sys.stdin.readline

N = int(put())
ant = '1'

if N <= 2:
    print(1)
elif N <= 5:
    print(2)
else:
    print(3)