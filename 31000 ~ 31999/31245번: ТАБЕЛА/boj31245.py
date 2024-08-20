# 백준 31245번 ТАБЕЛА
import sys
put = sys.stdin.readline

cena = put().split()
answer = "-"

for i in cena:
    if answer[-1] == i[0]:
        answer += '\'' + i[1:]
    else:
        answer += i

print(answer[1:])