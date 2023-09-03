# 백준 29614번 학점계산프로그램
import sys
put = sys.stdin.readline

S = put().strip()
score = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0, '+': .5}

s = n = 0
for i in S:
    if i.isalpha():
        n += 1
    s += score[i]

print(s / n)