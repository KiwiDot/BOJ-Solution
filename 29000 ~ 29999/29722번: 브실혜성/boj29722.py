# 백준 29722번 브실혜성
import sys
put = sys.stdin.readline

y, m, d = map(int, put().strip().split('-'))
N = int(put())

date = y * 360 + m * 30 + d + N
y, date = divmod(date, 360)
m, d = divmod(date, 30)

if not d:
    m -= 1
    d = 30

if not m:
    y -= 1
    m = 12

y, m, d = str(y).zfill(4), str(m).zfill(2), str(d).zfill(2)
print(y + '-' + m + '-' + d)