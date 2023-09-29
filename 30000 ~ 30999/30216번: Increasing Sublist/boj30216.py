# 백준 30216번 Increasing Sublist
import sys
put = sys.stdin.readline

n = int(put())
arr = list(map(int, put().split()))
answer = cnt = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        answer = max(answer, cnt)
        cnt = 1

answer = max(answer, cnt)
print(answer)