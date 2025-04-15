# 백준 7214번 Ateivių kojinės
import sys
put = sys.stdin.readline

k, s = map(int, put().split())
socks = list(map(int, put().split()))

answer = 1
for i in socks:
    answer += min(i, k-1)

print(answer)