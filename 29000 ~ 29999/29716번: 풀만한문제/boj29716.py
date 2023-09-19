# 백준 29716번 풀만한문제
import sys
put = sys.stdin.readline

J, N = map(int, put().split())
answer = 0

while N:
    N -= 1
    s = put().strip()
    size = 0

    for i in s:
        if i == ' ':
            size += 1
        elif i.isupper():
            size += 4
        else:
            size += 2

    if size <= J:
        answer += 1

print(answer)