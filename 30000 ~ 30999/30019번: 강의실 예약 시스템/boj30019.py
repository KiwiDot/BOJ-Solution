# 백준 30019번 강의실 예약 시스템
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
room = dict([(i+1, 0) for i in range(N)])

while M:
    M -= 1
    k, s, e = map(int, put().split())

    if room[k] <= s:
        print("YES")
        room[k] = e
    else:
        print("NO")