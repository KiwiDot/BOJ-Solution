# 백준 32888번 Consolidating Windows
import sys
from decimal import Decimal
put = sys.stdin.readline

a, b = map(int, put().split())

print(Decimal((a ** 2 + b ** 2) ** 0.5))