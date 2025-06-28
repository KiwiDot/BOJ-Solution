# 백준 14040번 Hidden Palindrome
import sys
put = sys.stdin.readline

s = put().strip()
answer = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j+1] == s[i:j+1][::-1]:
            answer = max(answer, j - i + 1)

print(answer)