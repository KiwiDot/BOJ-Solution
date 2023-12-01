# 백준 30886번 Artistic Souvenir
import sys
from math import pi
put = sys.stdin.readline

a = int(put())
r = (a / pi) ** 0.5

answer = (r * 2 + 2) ** 2
print("{:.10f}".format(answer))