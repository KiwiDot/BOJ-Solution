# 백준 22541번 Sum of Consecutive Integers
import sys
put = sys.stdin.readline

while True:
    N = int(put())
    if not N:
        break

    answer = 0
    for i in range(2, N):
        n = i * (i+1) // 2
        if n > N:
            break

        if (N - n) % i == 0:
            answer += 1

    print(answer)