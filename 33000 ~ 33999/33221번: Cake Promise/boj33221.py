# 백준 33221번 Cake Promise
import sys
put = sys.stdin.readline

t, p = map(int, put().split())

prof = [int(i) for i in put().strip().replace('X', '').split()]
time, solved = sum(prof), len(prof)

answer = 0
for i in range(t-1):
    stud = [int(i) for i in put().strip().replace('X', '').split()]
    tim, sol = sum(stud), len(stud)

    if sol > solved:
        answer += 1

    elif sol == solved and tim <= time:
        answer += 1

print(answer)