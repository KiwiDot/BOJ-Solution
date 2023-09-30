# 백준 7280번 Kortos
import sys
put = sys.stdin.readline

card = {put().strip() for i in range(51)}

for i in ['S', 'B', 'V', 'K']:
    for j in range(1, 14):
        if "{} {}".format(i, j) not in card:
            print("{} {}".format(i, j))