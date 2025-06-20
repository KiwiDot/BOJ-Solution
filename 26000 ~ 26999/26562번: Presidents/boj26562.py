# 백준 26562번 Presidents
import sys
put = sys.stdin.readline
money = {"Franklin": 100,
         "Grant": 50,
         "Jackson": 20,
         "Hamilton": 10,
         "Lincoln": 5,
         "Washington": 1}

n = int(put())

while n:
    n -= 1
    answer = 0
    p = put().split()
    for i in p:
        answer += money[i]

    print(f"${answer}")
