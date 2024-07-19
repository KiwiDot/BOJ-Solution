# 백준 32046번 Snacks within 300 Yen
import sys
put = sys.stdin.readline

while True:
    N = int(put())
    if not N:
        break

    a = list(map(int, put().split()))
    answer = 0

    for i in a:
        if answer + i <= 300:
            answer += i

    print(answer)