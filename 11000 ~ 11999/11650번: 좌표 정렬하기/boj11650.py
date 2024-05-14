# 백준 11650번 좌표 정렬하기
import sys
put = sys.stdin.readline

N = int(put())
xy = sorted([list(map(int, put().split())) for i in range(N)], key=lambda x: [x[0], x[1]])

for i in xy:
    print(*i)