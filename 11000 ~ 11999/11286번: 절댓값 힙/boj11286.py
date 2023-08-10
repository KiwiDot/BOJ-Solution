# 백준 11286번 절댓값 힙
import sys
from heapq import heappush, heappop
put = sys.stdin.readline

N = int(put())
dic = {}
arr = []

while N:
    N -= 1
    x = int(put())

    if x:
        heappush(arr, abs(x))
        if abs(x) not in dic:
            dic[abs(x)] = {-x: 0, x: 0}
        dic[abs(x)][x] += 1

    else:
        if arr:
            x = heappop(arr)
            if dic[x][-x]:
                dic[x][-x] -= 1
                print(-x)
            else:
                dic[x][x] -= 1
                print(x)

        else:
            print(0)