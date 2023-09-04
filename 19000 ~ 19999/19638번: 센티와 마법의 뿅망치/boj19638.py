# 백준 19638번 센티와 마법의 뿅망치
import sys
from heapq import heappop, heappush
put = sys.stdin.readline

N, centi, T = map(int, put().split())
H = []
cnt = 0

for i in range(N):
    heappush(H, -int(put()))

for i in range(T):
    h = -heappop(H)
    if h < centi:
        heappush(H, -h)
        break
    if h > 1:
        cnt += 1
        h //= 2

    heappush(H, -h)

h = -min(H)
if h < centi:
    print("YES")
    print(cnt)

else:
    print("NO")
    print(h)