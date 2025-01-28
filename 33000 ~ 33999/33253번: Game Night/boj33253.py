# 백준 33253번 Game Night
import sys
from collections import Counter
put = sys.stdin.readline

n = int(put())
pw_old = Counter(put().strip())
pw_new = Counter(put().strip())

answer = 0
for i in pw_new:
    if i not in pw_old:
        answer += pw_new[i]
        continue

    answer += max(0, pw_new[i] - pw_old[i])

print(answer)