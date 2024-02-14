# 백준 2200번 계산기
import sys
put = sys.stdin.readline

N = int(put())
data = list(map(int, put().split()))
answer = 2

for i in data[1:-1]:
    if i == 0:
        answer += 2
    else:
        answer += len(str(i)) + 3

if data[-1]:
    answer += len(str(data[-1])) + 1

print(answer)

