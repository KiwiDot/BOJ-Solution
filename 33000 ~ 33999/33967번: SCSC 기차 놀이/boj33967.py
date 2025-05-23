# 백준 33967번 SCSC 기차 놀이
import sys
put = sys.stdin.readline

N = int(put())
SCSC = put().strip()
answer = 0

for i in range(N):
    if SCSC[i] == '[':
        answer += 1

    if SCSC[i] == '5' or SCSC[i] == '2':
        answer += 1
        if SCSC[i-1] == ']' or SCSC[i-1] == SCSC[i]:
            answer += 1

    if SCSC[i-1] == SCSC[i] == ']':
        answer += 1

print(answer)