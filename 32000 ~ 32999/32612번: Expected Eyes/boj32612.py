# 백준 32612번 Expected Eyes
import sys
put = sys.stdin.readline


def dice(d, c):
    for i in range(1, x[d]+1):
        if d == n - 1:
            cnt[c+i] += 1
        else:
            dice(d+1, c+i)


n = int(put())
x = list(map(int, put().split()))
cnt = [0] * (sum(x) + 1)

dice(0, 0)
answer = 0

for i in range(sum(x) + 1):
    answer += cnt[i] * i

print(answer / sum(cnt))