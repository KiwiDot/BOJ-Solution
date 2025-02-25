# 백준 33541번 2025는 무엇이 특별할까?
import sys
put = sys.stdin.readline

X = int(put())

for year in range(X+1, 10000):
    y1, y2 = str(year)[:2], str(year)[2:]

    if (int(y1) + int(y2)) ** 2 == year:
        print(year)
        break

else:
    print(-1)
