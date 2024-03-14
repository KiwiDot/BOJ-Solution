# 백준 31609번 現れている数字 (Appearing Numbers)
import sys
put = sys.stdin.readline

N = int(put())
A = sorted(list(set(map(int, put().split()))))

for i in A:
    print(i)