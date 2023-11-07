# 백준 30395번 내 스트릭을 돌려내!
import sys
put = sys.stdin.readline

N = int(put())
P = list(map(int, put().split()))
item = True
used = 0
cnt = 0

answer = set()
for i in range(N):
    if not item and i == used + 2:
        item = True

    if P[i]:
        cnt += 1
    elif item:
        item = False
        used = i
    else:
        answer.add(cnt)
        cnt = 0

answer.add(cnt)
print(max(answer))