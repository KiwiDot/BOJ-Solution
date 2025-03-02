# 백준 29145번 Можно и отдохнуть
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
answer = 0

while n:
    n -= 1
    a, b, c = map(int, put().split())

    if (k - a) % b == 0 and k >= a:
        answer += c

print(answer)
