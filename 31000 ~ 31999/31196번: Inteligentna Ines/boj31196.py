# 백준 31196번 Inteligentna Ines
import sys
put = sys.stdin.readline

txt = put().strip()
n = len(txt)
r = s = 0

for r in range(1, n+1):
    s = n // r

    if r >= s and r * s == n:
        break

answer = [''] * r
for i in range(n):
    answer[i % s] += txt[i]

print(''.join(answer))
