# 백준 29875번 Imeline masin
import sys
put = sys.stdin.readline

N = int(put())
data = list(map(int, put().split()))
c = [1, 0, 0, 0]

for i in data:
    match i:
        case 0:
            c = c[1], c[0], 0, c[2] or c[3]
        case 1:
            c = c[3], c[0], c[1] or c[2], 0
        case -1:
            c = c[1] or c[3], c[0], c[1] or c[2], c[2] or c[3]

for i in c:
    print("JAH" if i else "EI")