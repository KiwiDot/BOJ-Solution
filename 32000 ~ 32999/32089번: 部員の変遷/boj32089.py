# 백준 32089번 部員の変遷
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break
    a = list(map(int, put().split()))
    answer = [sum(a[:3])]

    for i in range(3, n):
        answer.append(answer[-1] + a[i] - a[i-3])

    print(max(answer))