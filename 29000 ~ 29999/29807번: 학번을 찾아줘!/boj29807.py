# 백준 29807번 학번을 찾아줘!
import sys
put = sys.stdin.readline

T = int(put())
s = list(map(int, put().split())) + [0] * (5 - T)
answer = 0

answer += (s[0] - s[2]) * 508 if s[0] > s[2] else (s[2] - s[0]) * 108
answer += (s[1] - s[3]) * 212 if s[1] > s[3] else (s[3] - s[1]) * 305
answer += s[4] * 707

print(answer * 4763)