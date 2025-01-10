# 백준 29627번 Ноутбук
import sys
put = sys.stdin.readline

n, x, y = map(int, put().split())
time = [put().strip() for i in range(n)] + ["23:59"]
answer = 100.0
t = 0

for i in range(len(time)):
    h, m = map(int, time[i].split(':'))
    d = h * 60 + m - t

    if i % 2:
        answer -= 100 / x * d
    else:
        answer += 100 / y * d

    answer = min(answer, 100)
    answer = max(answer, 0)

    t = h * 60 + m

print(answer)

