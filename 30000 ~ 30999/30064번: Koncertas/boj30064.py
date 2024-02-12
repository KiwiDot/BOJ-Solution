# 백준 30064번 Koncertas
import sys
put = sys.stdin.readline

N = int(put())
num = list(map(int, put().split()))
answer = idx = 0

while num[idx]:
    idx = num[idx] - 1
    answer += 1

print(answer)

