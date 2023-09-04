# 백준 1522번 문자열 교환
import sys
put = sys.stdin.readline

s = put().strip()
n = len(s)
idx = s.count('a')

s += s
a = s[:idx].count('a')
b = idx - a
answer = b

for i in range(idx, n+idx):
    if s[i-idx] == 'a':
        a -= 1
    else:
        b -= 1

    if s[i] == 'a':
        a += 1
    else:
        b += 1

    answer = min(answer, b)

print(answer)