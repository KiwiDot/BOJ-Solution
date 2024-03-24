# 백준 29344번 Спичрайтер Йоды
import sys
put = sys.stdin.readline

s = put().strip().split('.')
answer = []

for i in s:
    if i:
        answer.append(' '.join(i.strip().split()[::-1]) + '.')

print(*answer)
