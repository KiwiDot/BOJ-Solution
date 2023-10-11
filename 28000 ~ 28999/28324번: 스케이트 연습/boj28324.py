# 백준 28324번 스케이트 연습
import sys
put = sys.stdin.readline

N = int(put())
V = list(map(int, put().split()))[::-1]

v = answer = 0
for i in range(N):
    v = min(v + 1, V[i])
    answer += v

print(answer)