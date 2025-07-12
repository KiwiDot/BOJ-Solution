# 백준 7217번 Šampūnas
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
h = {int(put()) for i in range(K)}

answer = 0
check = True

for i in range(1, N+1):
    if i == 1 or i in h or not check:
        answer += 1
        check = True
    else:
        check = False

print(answer)
