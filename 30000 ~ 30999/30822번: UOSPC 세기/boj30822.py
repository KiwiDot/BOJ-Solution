# 백준 30822번 UOSPC 세기
import sys
put = sys.stdin.readline

n = int(put())
S = put().strip()

cnt = {'u': 0, 'o': 0, 's': 0, 'p': 0, 'c': 0}
for i in S:
    if i in cnt:
        cnt[i] += 1

print(min(cnt.values()))