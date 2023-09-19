# 백준 30018번 타슈
import sys
put = sys.stdin.readline

N = int(put())
a = list(map(int, put().split()))
b = list(map(int, put().split()))

answer = sum([abs(a[i] - b[i]) for i in range(N)]) // 2
print(answer)