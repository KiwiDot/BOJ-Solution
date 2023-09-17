# 백준 29752번 최장 스트릭
import sys
put = sys.stdin.readline

N = int(put())
s = list(map(int, put().split()))

answer = cnt = 0
for i in s:
    if i == 0:
        answer = max(answer, cnt)
        cnt = 0
    else:
        cnt += 1

answer = max(answer, cnt)
print(answer)