# 백준 30329번 Kick
import sys
put = sys.stdin.readline

s = put().strip()

answer = 0
for i in range(len(s) - 3):
    if s[i:i+4] == "kick":
        answer += 1

print(answer)