# 백준 32855번 Which One is Larger
import sys
from decimal import Decimal
put = sys.stdin.readline

a = put().strip()
b = put().strip()

da = Decimal(a)
db = Decimal(b)

ta = tuple(map(int, a.split('.')))
tb = tuple(map(int, b.split('.')))

if da > db:
    d = 1
elif da < db:
    d = 2
else:
    d = 3

if ta > tb:
    t = 1
elif ta < tb:
    t = 2
else:
    t = 3

if d == t:
    print(max(da, db))
else:
    print(-1)
