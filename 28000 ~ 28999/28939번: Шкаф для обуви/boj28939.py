# 백준 28939번 Шкаф для обуви
import sys
put = sys.stdin.readline

n = int(put())
k, m1, m2 = map(int, put().split())
answer = 0

while n:
    n -= 1
    data = list(map(int, put().split()))
    h = data[0]
    ki = data[1]
    s = data[2:]

    for i in s:
        h1 = max(h, i * m2)
        h2 = min(h * k, i * m1)

        if h1 > h2:
            answer += 1

print(answer)
