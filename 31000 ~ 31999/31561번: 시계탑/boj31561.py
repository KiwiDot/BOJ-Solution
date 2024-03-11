# 백준 31561번 시계탑
import sys
put = sys.stdin.readline

M = int(put())

if M <= 30:
    answer = M / 2
else:
    answer = 15 + (M - 30) * 3 / 2

print("{:.1f}".format(answer))