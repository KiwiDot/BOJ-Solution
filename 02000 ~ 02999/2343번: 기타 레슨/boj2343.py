# 백준 2343번 기타 레슨
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
t = list(map(int, put().split()))

start, end = max(t), 10 ** 10
answer = 0

while start <= end:
    mid = (start + end) // 2
    m = 0
    n = 0

    for i in t:
        if n >= i:
            n -= i
        else:
            m += 1
            n = mid - i

    if m <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)