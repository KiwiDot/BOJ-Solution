# 백준 31242번 ШАХМАТНА ДЪСКA
import sys
put = sys.stdin.readline

chess = {}

for i in range(4):
    num = list(map(int, put().split()))
    for j in range(5):
        chess[num[j]] = (i, j)

for i in range(2, 21):
    xi, yi = chess[i]
    xj, yj = chess[i-1]

    z = (xi - xj) ** 2 + (yi - yj) ** 2
    if z != 5:
        print(i-1)
        break
else:
    print(20)