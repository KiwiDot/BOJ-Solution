# 백준 11687번 팩토리얼 0의 개수
import sys
put = sys.stdin.readline

M = int(put())
start = -1
mid = 0
end = 1_000_000_000_001

while start + 1 < end:
    mid = (start + end) // 2
    m = 0
    n = 5

    while n <= mid:
        m += mid // n
        n *= 5

    if m >= M:
        end = mid
    else:
        start = mid

answer = set()
for i in [start, mid, end]:
    m = 0
    n = 5

    while n <= i:
        m += i // n
        n *= 5

    if m == M:
        answer.add(i)

if answer:
    print(min(answer))
else:
    print(-1)