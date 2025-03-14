# 백준 7215번 Ateivių kojinės
import sys
put = sys.stdin.readline

k, s = map(int, put().split())
m = list(map(int, put().split()))

answer = 0
check = True
for i in m:
    answer += min(i, k-1)
    if i >= k:
        check = False

print(-1 if check else answer + 1)