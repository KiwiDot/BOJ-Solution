# 백준 33653번 Search Wizard
import sys
put = sys.stdin.readline

W = put().strip()
M = map(int, put().split())
S = put().split()

answer = 0
for s in S:
    for i in range(len(s) - len(W) + 1):
        if W == s[i:i+len(W)]:
            answer += 1

print(answer)