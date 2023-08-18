# 백준 11497번 통나무 건너뛰기
import sys
from collections import deque
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())
    L = sorted(list(map(int, put().split())))

    arr = deque([L.pop()])
    while L:
        arr.append(L.pop())
        if L:
            arr.appendleft(L.pop())

    answer = max([abs(arr[i] - arr[i-1]) for i in range(N)])
    print(answer)