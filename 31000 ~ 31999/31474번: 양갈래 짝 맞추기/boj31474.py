# 백준 31474번 양갈래 짝 맞추기
import sys
put = sys.stdin.readline

N = int(put())
answer = 1

for i in range(2, N + 1, 2):
    answer *= i - 1

print(answer)