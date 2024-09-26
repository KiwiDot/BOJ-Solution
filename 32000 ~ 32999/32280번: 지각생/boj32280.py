# 백준 32280번 지각생
import sys
put = sys.stdin.readline
job = {'teacher': 0, 'student': 1}

N = int(put())
data = sorted([put().split() for i in range(N+1)], key=lambda x: [x[0], job[x[1]]])
t = put().strip()
check = answer = 0

for i in data:
    if i[1] == 'teacher':
        check = 1
    elif check and i[0] >= t:
        answer += 1

print(answer)