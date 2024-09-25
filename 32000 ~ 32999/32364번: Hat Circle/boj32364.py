# 백준 32364번 Hat Circle
import sys
put = sys.stdin.readline

N = int(put())
H = [int(put()) for i in range(N)]
n = N // 2

answer = 0
for i in range(n):
    if H[i] == H[(i + n) % N]:
        answer += 2

print(answer)