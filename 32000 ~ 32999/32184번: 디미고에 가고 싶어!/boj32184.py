# 백준 32184번 디미고에 가고 싶어!
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
answer = set()

for i in range(A, B+1):
    if i % 2:
        answer.add(i + 1)
    else:
        answer.add(i)

print(len(answer))