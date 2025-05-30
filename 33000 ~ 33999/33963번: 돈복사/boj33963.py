# 백준 33963번 돈복사
import sys
put = sys.stdin.readline

N = int(put())
n = len(str(N))
answer = 0

for i in range(1, 4):
    if n != len(str(N * 2 ** i)):
        break
    answer += 1

print(answer)