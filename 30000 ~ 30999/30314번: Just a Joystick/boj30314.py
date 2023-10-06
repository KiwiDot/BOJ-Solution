# 백준 30314번 Just a Joystick
import sys
put = sys.stdin.readline

n = int(put())
s1 = put().strip()
s2 = put().strip()

answer = 0
for i in range(n):
    move = abs(ord(s1[i]) - ord(s2[i]))
    answer += min(move, 26 - move)

print(answer)