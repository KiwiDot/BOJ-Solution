# 백준 30793번 gahui and sousenkyo 3
import sys
from decimal import Decimal
put = sys.stdin.readline

p, r = map(int, put().split())

v = Decimal(p / r)

if v < 0.2:
    print("weak")
elif v < 0.4:
    print("normal")
elif v < 0.6:
    print("strong")
else:
    print("very strong")