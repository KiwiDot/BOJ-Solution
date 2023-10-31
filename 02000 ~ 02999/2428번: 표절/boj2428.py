# 백준 2428번 표절
import sys
put = sys.stdin.readline

N = int(put())
size = sorted(list(map(int, put().split())))
answer = 0

for i in range(N):
    s, e = 0, i-1

    a = i
    while s <= e:
        m = (s + e) // 2

        if size[m] >= 0.9 * size[i]:
            a = m
            e = m - 1
        else:
            s = m + 1

    answer += i - a

print(answer)