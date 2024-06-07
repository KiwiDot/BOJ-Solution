# 백준 31882번 근수
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
answer = n = 0

for i in S:
    if i == '2':
        n += 1
        answer += n * (n + 1) // 2
    else:
        n = 0

print(answer)