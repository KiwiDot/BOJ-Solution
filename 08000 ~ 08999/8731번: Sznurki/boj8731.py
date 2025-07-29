# 백준 8731번 Sznurki
import sys
put = sys.stdin.readline

n, w = map(int, put().split())
a = list(map(int, put().split()))

answer = check = 0

for i in a:
    check += i
    if check >= w:
        answer += 1
        check = 0

print(answer)
