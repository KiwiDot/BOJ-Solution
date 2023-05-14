# 백준 1009번 분산처리
import sys
put = sys.stdin.readline
digit = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
         [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

T = int(put())

while T:
    T -= 1
    a, b = map(int, put().split())
    num = digit[a % 10]

    print(num[b % len(num) - 1])
