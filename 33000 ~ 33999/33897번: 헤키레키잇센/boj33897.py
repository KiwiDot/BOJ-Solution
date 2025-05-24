# 백준 33897번 헤키레키잇센
import sys
put = sys.stdin.readline

N = int(put())
data = list(map(int, put().split()))
cnt = 1
maximum = m = n = 0

for i in data:
    if i < n:
        maximum = max(maximum, m)
        cnt += 1
        m = 1
    else:
        m += 1

    n = i

maximum = max(maximum, m)
print(cnt, maximum)