# 백준 32400번 다트판
import sys
put = sys.stdin.readline

num = list(map(int, put().split()))

i = num.index(20)
Alice = (num[i-1] + num[i] + num[(i+1)%20]) / 3
Bob = sum(num) / 20

if Alice > Bob:
    print('Alice')
elif Alice < Bob:
    print('Bob')
else:
    print('Tie')