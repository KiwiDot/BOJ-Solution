# 백준 30214번 An Easy-Peasy Problem
import sys
put = sys.stdin.readline

s1, s2 = map(int, put().split())

if s1 >= s2 / 2:
    print('E')
else:
    print('H')