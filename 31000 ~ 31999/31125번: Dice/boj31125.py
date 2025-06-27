# 백준 31125번 Dice
import sys
put = sys.stdin.readline

B = int(input())

while B:
    B -= 1
    S, n, f, m = map(int, put().split())

    if n + m <= S <= n * f + m:
        print("YES")
    else:
        print("NO")
