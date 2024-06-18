# 백준 31962번 등교
import sys
put = sys.stdin.readline

N, X = map(int, put().split())
answer = [-1]

while N:
    N -= 1
    S, T = map(int, put().split())
    if S + T <= X:
        answer.append(S)

print(max(answer))