# 백준 8321번 Tables
import sys
put = sys.stdin.readline

n, k, s = map(int, put().split())
a = sorted(list(map(int, put().split())), reverse=True)

answer = cnt = 0

for i in a:
    cnt += i
    answer += 1
    if cnt >= k * s:
        break

print(answer)
