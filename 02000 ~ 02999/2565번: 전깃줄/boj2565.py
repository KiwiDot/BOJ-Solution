# 백준 2565번 전깃줄
import sys
put = sys.stdin.readline

n = int(put())
data = sorted([list(map(int, put().split())) for i in range(n)], key=lambda x: [x[0], x[1]])
answer = []

for A, B in data:
    check = {1}
    for b, cnt in answer:
        if b < B:
            check.add(cnt + 1)

    answer.append((B, max(check)))

print(n - max([i[1] for i in answer]))