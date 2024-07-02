# 백준 29534번 Буквы и весы
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()
answer = 0

for i in s:
    answer += ord(i) - 96

if len(s) <= n:
    print(answer)
else:
    print("Impossible")