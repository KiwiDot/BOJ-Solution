# 백준 31796번 한빛미디어 (Easy)
import sys
put = sys.stdin.readline

N = int(put())
S = sorted(list(map(int, put().split())))
answer = price = 0

for i in S:
    if i >= price * 2:
        answer += 1
        price = i

print(answer)