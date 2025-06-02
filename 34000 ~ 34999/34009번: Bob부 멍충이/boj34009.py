# 백준 34009번 Bob부 멍충이
import sys
put = sys.stdin.readline

N = int(put())
A = sorted(list(map(int, put().split())), reverse=True)

if N % 2:
    print('Bob')
else:
    print('Alice')