# 백준 31798번 단원평가
import sys
put = sys.stdin.readline

a, b, c = map(int, put().split())

if a == 0 or b == 0:
    answer = c ** 2 - a - b
else:
    answer = int((a + b) ** 0.5)

print(answer)