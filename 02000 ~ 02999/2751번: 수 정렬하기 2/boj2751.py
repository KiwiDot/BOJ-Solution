# 백준 2751번 수 정렬하기 2
import sys
put = sys.stdin.readline

N = int(put())
n = sorted([int(put()) for i in range(N)])

for i in n:
    print(i)