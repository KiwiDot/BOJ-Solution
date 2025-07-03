# 백준 24375번 ПОДНИЗ
import sys
put = sys.stdin.readline

a = put().strip()
b = put().strip()

A = [0] * 26
B = [0] * 26

for i in a:
    A[ord(i)-97] += 1
for i in b:
    B[ord(i)-97] += 1

answer = ''

for i in range(26):
    m = min(A[i], B[i])
    answer += chr(i+97) * m

print(answer)
