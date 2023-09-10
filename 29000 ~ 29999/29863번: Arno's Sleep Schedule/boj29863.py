# 백준 29863번 Arno's Sleep Schedule
import sys
put = sys.stdin.readline

t1 = int(put())
t2 = int(put())

answer = t2 - t1
if answer < 0:
    answer += 24

print(answer)