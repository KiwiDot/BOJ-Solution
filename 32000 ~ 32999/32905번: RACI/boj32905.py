# 백준 32905번 RACI
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
answer = "Yes"

while n:
    n -= 1
    text = put().split()
    if text.count('A') != 1:
        answer = "No"

print(answer)