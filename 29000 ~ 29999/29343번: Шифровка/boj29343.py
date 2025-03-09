# 백준 29343번 Шифровка
import sys
put = sys.stdin.readline

n = int(put())
text = put().strip().lower()
vowels = {'a', 'e', 'i', 'o', 'u'}

pre = [0]
suf = [0]

for i in range(n):
    pre.append(pre[-1] + int(text[i] in vowels))
    suf.append(suf[-1] + int(text[n-i-1] in vowels))

answer = 0
for i in range(n+1):
    if pre[i] and pre[i] == suf[i]:
        answer += 1

print(answer)