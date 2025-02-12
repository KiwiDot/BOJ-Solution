# 백준 27222번 Штангист
import sys
put = sys.stdin.readline

n = int(put())
d = list(map(int, put().split()))

answer = 0
for i in d:
    x, y = list(map(int, put().split()))

    if i and y > x:
        answer += y - x

print(answer)