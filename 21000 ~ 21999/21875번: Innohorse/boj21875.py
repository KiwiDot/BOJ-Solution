# 백준 21875번 Innohorse
import sys
put = sys.stdin.readline

xy1 = put().strip()
xy2 = put().strip()

x = abs(ord(xy1[0]) - ord(xy2[0]))
y = abs(int(xy1[1]) - int(xy2[1]))

print(*sorted([x, y]))