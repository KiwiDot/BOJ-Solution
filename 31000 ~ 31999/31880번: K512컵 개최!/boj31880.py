# 백준 31880번 K512컵 개최!
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
a = list(map(int, put().split()))
b = sorted(list(map(int, put().split())))

answer = sum(a)
for i in b:
    if i:
        answer *= i

print(answer)