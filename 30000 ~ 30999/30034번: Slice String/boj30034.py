# 백준 30034번 Slice String
import sys
put = sys.stdin.readline

N = int(put())
n = set(put().split())

M = int(put())
m = set(put().split())

K = int(put())
k = set(put().split())

S = int(put())
s = put().strip()

n -= k
m -= k
answer = ""

for i in s:
    if i in n or i in m:
        answer += ' '
    else:
        answer += i

for i in answer.split():
    print(i)