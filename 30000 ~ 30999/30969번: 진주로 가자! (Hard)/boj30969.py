# 백준 30969번 진주로 가자! (Hard)
import sys
put = sys.stdin.readline


N = int(put())
jinju = 0
money = [0] * 1002

while N:
    N -= 1
    D, C = put().split()
    if D == "jinju":
        jinju = int(C)
    elif 1 <= int(C) <= 1000:
        money[int(C)] += 1
    else:
        money[-1] += 1

answer = sum(money[jinju+1:])

print(jinju)
print(answer)