# 백준 29300번 Назначения
import sys
put = sys.stdin.readline

s = put().strip()
c = set(s)
answer = set()

for i in c:
    answer.add(s.replace(i, ''))

print(min(answer))