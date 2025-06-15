# 백준 25802번 Fiborooji Sequence
import sys
put = sys.stdin.readline

a, b = map(int, input().split())
x, y = a, b
answer = 2

while True:
    x, y = y, (x + y) % 10
    answer += 1
    if x == a and y == b:
        break

print(answer)






