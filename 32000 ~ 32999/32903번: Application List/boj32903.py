# 백준 32903번 Application List
import sys
put = sys.stdin.readline

n = int(put())
name = {put().strip()[0] for i in range(n)}
answer = ["."] * 26

for i in range(26):
    if chr(i + 97) in name:
        answer[i] = chr(i + 97)

for i in range(5):
    print(''.join(answer[i*6:i*6+6]))