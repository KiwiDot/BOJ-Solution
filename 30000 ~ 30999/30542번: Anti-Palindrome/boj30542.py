# 백준 30542번 Anti-Palindrome
import sys
put = sys.stdin.readline

text = ''.join(put().split()).lower()
answer = "Anti-palindrome"

for i in range(len(text)-1):
    t1 = text[i:i+2]
    t2 = text[i:i+3]

    if t1 == t1[::-1] or t2 == t2[::-1]:
        answer = "Palindrome"

print(answer)