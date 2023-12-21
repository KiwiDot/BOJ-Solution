# 백준 30958번 서울사이버대학을 다니고
import sys
put = sys.stdin.readline

N = int(put())
song = put().strip().upper()
cnt = dict([(chr(i+65), 0) for i in range(26)])

for i in song:
    if i.isalpha():
        cnt[i] += 1

print(max(cnt.values()))