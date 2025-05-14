# 백준 33835번 도로 공사
import sys
put = sys.stdin.readline

N = int(put())
xy = [list(map(int, put().split())) for i in range(N)]

x1, y1 = xy[0]
xN, yN = xy[-1]

print(((x1 - xN) ** 2 + (y1 - yN) ** 2) ** 0.5)