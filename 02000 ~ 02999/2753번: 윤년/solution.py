# 백준 2753번 윤년
import sys
put = sys.stdin.readline

year = int(put())

if not year % 400 or (year % 100 and not year % 4):
    print(1)
else:
    print(0)
