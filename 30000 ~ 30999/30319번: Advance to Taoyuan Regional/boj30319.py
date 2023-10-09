# 백준 30319번 Advance to Taoyuan Regional
import sys
put = sys.stdin.readline

date = put().strip()
answer = sorted([date, "2023-09-16"])

if answer[0] == date:
    print("GOOD")
else:
    print("TOO LATE")