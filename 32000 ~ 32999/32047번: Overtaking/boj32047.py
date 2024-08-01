# 백준 32047번 Overtaking
import sys
put = sys.stdin.readline

while True:
    N = int(put())
    if not N:
        break
    a = list(map(int, put().split()))
    b = list(map(int, put().split()))

    answer = A = B = 0
    win = '-'

    for i in range(N):
        A += a[i]
        B += b[i]

        if win != 'A' and A > B:
            answer += 1
            win = 'A'

        elif win != 'B' and B > A:
            answer += 1
            win = 'B'

    print(answer - 1 if answer else 0)