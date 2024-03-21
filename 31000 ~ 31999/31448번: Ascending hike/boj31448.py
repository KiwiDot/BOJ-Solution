# 백준 31448번 Ascending hike
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
a = [10 ** 18, 10 ** 18]
answer = 0

for i in A:
    if i > a[1]:
        a[1] = i
    else:
        answer = max(answer, a[1] - a[0])
        a = [i, i]
answer = max(answer, a[1] - a[0])

print(answer)