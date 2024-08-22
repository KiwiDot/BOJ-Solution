# 백준 26536번 Cowspeak
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    s = put().split()
    answer = ""

    for i in s:
        si = i.count('M') * 16 + i.count('O')
        answer += chr(si)

    print(answer)