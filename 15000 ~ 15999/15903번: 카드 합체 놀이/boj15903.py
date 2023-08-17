# 백준 15903번 카드 합체 놀이
import sys
from heapq import heappush, heappop
put = sys.stdin.readline

n, m = map(int, put().split())
a = list(map(int, put().split()))

heap = []
for i in a:
    heappush(heap, i)

while m:
    m -= 1
    x = heappop(heap)
    y = heappop(heap)

    heappush(heap, x + y)
    heappush(heap, x + y)

print(sum(heap))