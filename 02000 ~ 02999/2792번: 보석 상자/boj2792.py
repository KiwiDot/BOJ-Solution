# 백준 2792번 보석 상자
import sys
from math import ceil
put = sys.stdin.readline

N, M = map(int, put().split())
jewel = [int(put()) for i in range(M)]

start = 1
end = max(jewel)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([ceil(i / mid) for i in jewel])

    if cnt <= N:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)