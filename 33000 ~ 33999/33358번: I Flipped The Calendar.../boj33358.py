# 백준 33358번 I Flipped The Calendar...
import sys
from math import ceil
put = sys.stdin.readline

year = int(put())
month = [31, 28, 31, 30, 31, 30,
         31, 31, 30, 31, 30, 31]

# 1970년 1월 1일은 목요일부터 시작
d = 3

for y in range(1970, year+1):
    if y % 400 == 0 or (y % 4 == 0 and y % 100):
        month[1] = 29

    answer = 0
    for i in month:
        day = i + d
        answer += ceil(day / 7)
        d = day % 7

    month[1] = 28

print(answer)
