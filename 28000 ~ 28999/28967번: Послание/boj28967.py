# 백준 28967번 Послание
import sys
put = sys.stdin.readline

c = put().strip()
s = put().strip()
idx = answer = 0

for i in s:
    if c[idx] == i:
        idx += 1
        if idx == len(c):
            answer += 1
            idx = 0

print(answer)
