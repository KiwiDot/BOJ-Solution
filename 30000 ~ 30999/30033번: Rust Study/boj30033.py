# 백준 30033번 Rust Study
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
B = list(map(int, put().split()))

print(sum([A[i] <= B[i] for i in range(N)]))