# 백준 33168번 三角足し算 (Triangle Addition)
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

while len(A) > 1:
    A = [A[i] + A[i+1] for i in range(len(A)-1)]
    print(*A)