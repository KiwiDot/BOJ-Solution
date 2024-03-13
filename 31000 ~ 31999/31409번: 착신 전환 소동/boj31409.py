# 백준 31409번 착신 전환 소동
import sys
put = sys.stdin.readline

N = int(put())
a = list(map(int, put().split()))
call = []

for i in range(N):
    if i+1 != a[i]:
        call.append(i+1)

if len(call) == 0:
    answer = N
    a = [2] + [1] * (N-1)
else:
    answer = 0
    for i in range(N):
        if i+1 not in call:
            answer += 1
            a[i] = call[0]

print(answer)
print(*a)