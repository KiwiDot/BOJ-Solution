# 백준 32626번 SPC에 가는 길
import sys
put = sys.stdin.readline

Sx, Sy = map(int, put().split())
Ex, Ey = map(int, put().split())
Px, Py = map(int, put().split())

Sx, Ex = min(Sx, Ex), max(Sx, Ex)
Sy, Ey = min(Sy, Ey), max(Sy, Ey)

if Sx == Px == Ex or Sy == Py == Ey:
    if Sx < Px < Ex or Sy < Py < Ey:
        print(2)
    else:
        print(0)

elif Sx == Ex or Sy == Ey:
    print(0)

else:
    print(1)