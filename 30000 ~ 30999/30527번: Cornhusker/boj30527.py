# 백준 30527번 Cornhusker
import sys
put = sys.stdin.readline

data = list(map(int, put().split()))
N, KWF = map(int, put().split())

cnt = 0
for i in range(0, 10, 2):
    A = data[i]
    L = data[i+1]
    cnt += A * L

answer = cnt // 5 * N // KWF
print(answer)
