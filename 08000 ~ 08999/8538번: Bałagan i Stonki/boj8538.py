# 백준 8538번 Bałagan i Stonki
import sys
put = sys.stdin.readline

j = int(put())
cnt = set()

while j:
    j -= 1
    text = put().strip().lower()

    cnt.add(''.join(text.split('-')))

print(len(cnt))