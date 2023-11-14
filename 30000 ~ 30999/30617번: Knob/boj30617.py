# 백준 30617번 Knob
import sys
put = sys.stdin.readline

T = int(put())
l = r = 0

answer = 0
while T:
    T -= 1
    li, ri = map(int, put().split())

    if li and li == l:
        answer += 1
    if ri and ri == r:
        answer += 1
    if li and li == ri:
        answer += 1
    l, r = li, ri

print(answer)