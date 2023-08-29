# 백준 7571번 점 모으기
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
x, y = [], []

for i in range(M):
    xi, yi = map(int, put().split())
    x.append(xi)
    y.append(yi)

x.sort()
y.sort()

if M % 2:
    x1, y1 = x[M//2], y[M//2]
    answer = sum([abs(x1 - i) for i in x]) + sum([abs(y1 - i) for i in y])
    print(answer)

else:
    x1, y1 = x[M//2], y[M//2]
    x2, y2 = x[M//2-1], y[M//2-1]
    answer1 = sum([abs(x1 - i) for i in x]) + sum([abs(y2 - i) for i in y])
    answer2 = sum([abs(x2 - i) for i in x]) + sum([abs(y2 - i) for i in y])
    print(min(answer1, answer2))