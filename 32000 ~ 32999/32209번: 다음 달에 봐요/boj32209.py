# 백준 32209번 다음 달에 봐요
import sys
put = sys.stdin.readline

Q = int(put())
q = 0

while Q:
    Q -= 1
    n, xy = map(int, put().split())

    match n:
        case 1:
            q += xy

        case 2:
            if q < xy:
                print("Adios")
                break
            else:
                q -= xy

else:
    print("See you next month")