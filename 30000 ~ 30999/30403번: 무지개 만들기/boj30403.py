# 백준 30403번 무지개 만들기
import sys
put = sys.stdin.readline

rainbow = set("roygbiv")
RAINBOW = set("ROYGBIV")
N = int(put())
s = set(put().strip())

if s & rainbow == rainbow and s & RAINBOW == RAINBOW:
    print("YeS")
elif s & rainbow == rainbow:
    print("yes")
elif s & RAINBOW == RAINBOW:
    print("YES")
else:
    print("NO!")