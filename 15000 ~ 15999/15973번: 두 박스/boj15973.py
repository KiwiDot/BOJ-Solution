# 백준 15973번 두 박스
import sys
put = sys.stdin.readline

P = list(map(int, put().split()))
Q = list(map(int, put().split()))

x1 = max(P[0], Q[0])
y1 = max(P[1], Q[1])
x2 = min(P[2], Q[2])
y2 = min(P[3], Q[3])

dx = x2 - x1
dy = y2 - y1

if dx < 0 or dy < 0:
    print("NULL")
elif dx == 0 and dy == 0:
    print("POINT")
elif dx == 0 or dy == 0:
    print("LINE")
else:
    print("FACE")