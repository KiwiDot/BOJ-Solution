# 백준 11773번 ESEJ
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
answer = []

for i in range(B):
    answer.append(''.join([chr(int(i)+97) for i in str(i)]))

print(*answer)