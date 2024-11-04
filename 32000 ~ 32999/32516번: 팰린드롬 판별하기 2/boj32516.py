# 백준 32516번 팰린드롬 판별하기 2
import sys
put = sys.stdin.readline

N = int(put())
T = put().strip()
n = [set() for i in range(N//2)]

for i in range(N//2):
    n[i] |= {T[i], T[-i-1]}

answer = 0
for i in n:
    if len(i) == 2:
        if '?' in i:
            answer += 1
        else:
            answer = 0
            break

    elif len(i) == 1 and '?' in i:
        answer += 26

print(answer)