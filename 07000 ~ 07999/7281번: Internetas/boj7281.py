# 백준 7281번 Internetas
import sys
put = sys.stdin.readline

N = int(put())
T, M = map(int, put().split())
t, cnt = T, 0

answer = set()
for i in range(N-1):
    T, M = map(int, put().split())
    if M == 0:
        continue
    else:
        answer.add(T - t)
        t = T

print(max(answer))