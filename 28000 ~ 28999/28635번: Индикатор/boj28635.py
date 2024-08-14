# 백준 28635번 Индикатор
import sys
put = sys.stdin.readline

m, a, b = [int(put()) for i in range(3)]

if a > b:
    answer = m - a + b
else:
    answer = b - a

print(answer)