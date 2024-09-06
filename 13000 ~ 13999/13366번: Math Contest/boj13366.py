# 백준 13366번 Math Contest
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    x = sum([int(i) for i in put().strip()])

    print("YES" if not x % 9 else "NO")