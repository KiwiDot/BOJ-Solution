# 백준 11609번 Class Time
import sys
put = sys.stdin.readline

n = int(put())
name = [put().split() for i in range(n)]

name.sort(key=lambda x: [x[1], x[0]])

for i in name:
    print(*i)