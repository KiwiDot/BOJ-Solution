# 백준 31822번 재수강
import sys
put = sys.stdin.readline

target = put().strip()[:5]
N = int(put())
answer = 0

while N:
    N -= 1
    text = put().strip()[:5]

    if text == target:
        answer += 1

print(answer)