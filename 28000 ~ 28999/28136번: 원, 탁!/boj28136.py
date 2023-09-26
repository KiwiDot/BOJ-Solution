# 백준 28136번 원, 탁!
import sys
put = sys.stdin.readline

N = int(put())
a = list(map(int, put().split()))
a.append(a[0])

answer = 0
for i in range(1, N+1):
    if a[i] <= a[i-1]:
        answer += 1

print(answer)