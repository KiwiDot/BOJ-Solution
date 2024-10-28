# 백준 32560번 Amalgram
import sys
put = sys.stdin.readline

a = put().strip()
b = put().strip()
answer = ""

for i in range(26):
    c = chr(i+97)
    ac, bc = a.count(c), b.count(c)
    answer += c * max(ac, bc)

print(answer)