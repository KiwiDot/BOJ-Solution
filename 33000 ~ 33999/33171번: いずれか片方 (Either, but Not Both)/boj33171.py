# 백준 33171번 いずれか片方 (Either, but Not Both)
import sys
put = sys.stdin.readline

N = int(put())
A = int(put())
B = int(put())

answer = 0
for i in range(1, N+1):
    if i % A == i % B == 0:
        continue

    if i % A == 0 or i % B == 0:
        answer += 1

print(answer)