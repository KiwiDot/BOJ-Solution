# 백준 32225번 Glass Reflection
import sys
put = sys.stdin.readline

text = put().strip()
answer = []
t = ""

for i in text:
    if i == t:
        answer.append(i)
    else:
        t = i

print(''.join(answer))