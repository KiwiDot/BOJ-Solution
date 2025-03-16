# 백준 33571번 구멍
import sys
put = sys.stdin.readline

a0 = 'CcEFfGHhIiJjKkLlMmNnrSsTtUuVvWwXxYyZz '
a1 = 'AabDdegOoPpQqR@'
a2 = 'B'
a = [a0, a1, a2]

cnt = {}
for i in range(3):
    for j in a[i]:
        cnt[j] = i

S = put().strip()
answer = sum(cnt[i] for i in S)
print(answer)