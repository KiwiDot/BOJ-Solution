# 백준 1072번 게임
import sys
put = sys.stdin.readline

X, Y = map(int, put().split())
rate = Y * 100 // X

x = 0
start, end = 0, 10 ** 9
answer = -1

while start <= end:
    mid = (start + end) // 2

    new_rate = (Y + mid) * 100 // (X + mid)
    if rate != new_rate:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)