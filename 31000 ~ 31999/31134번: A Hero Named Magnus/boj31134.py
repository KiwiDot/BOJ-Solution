# 백준 31134번 A Hero Named Magnus
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    x = int(put())

    print((x - 1) * 2 + 1)