# 백준 29483번 Химия
import sys
put = sys.stdin.readline

s = put().strip()
n = {'H': 1, 'C': 12, 'N': 14, 'O': 16}
element = []

for i in s:
    if i.isalpha():
        element.append(i)
    else:
        element[-1] += i

answer = 0
for i in element:
    if len(i) == 1:
        answer += n[i]
    else:
        answer += n[i[0]] * int(i[1:])

print(answer)