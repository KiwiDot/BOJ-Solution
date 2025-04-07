# 백준 31257번 СИМЕТРИЧНА РЕДИЦА
import sys
put = sys.stdin.readline

N = int(put())
text = put().strip()
cnt = 0
answer = ''

for i in range(N):
    if text + answer == (text + answer)[::-1]:
        break
    cnt += 1
    answer = text[i] + answer

print(cnt)
if answer:
    print(answer)