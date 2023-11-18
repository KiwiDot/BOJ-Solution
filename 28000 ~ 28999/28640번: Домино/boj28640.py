# 백준 28640번 Домино
import sys
put = sys.stdin.readline

data1 = set(put().strip().split('|'))
data2 = set(put().strip().split('|'))

if data1 & data2:
    print("Yes")
else:
    print("No")