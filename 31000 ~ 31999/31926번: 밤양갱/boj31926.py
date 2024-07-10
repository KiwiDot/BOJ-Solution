# 백준 31926번 밤양갱
import sys
put = sys.stdin.readline

N = int(put())
answer = 0

# daldidalgo
daldidalgo = 1
answer += 8

# daldaidalgo 반복
while daldidalgo < N:
    daldidalgo *= 2
    answer += 1

# daldidan
if daldidalgo == N:
    answer += 1
answer += 1

print(answer)
