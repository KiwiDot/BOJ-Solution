# 백준 31823번 악질 검거
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
answer = set()
user = []

while N:
    N -= 1
    data = put().split()
    name = data.pop()
    cnt = count = 0

    for i in data:
        if i == '.':
            cnt += 1
        else:
            count = max(count, cnt)
            cnt = 0
    count = max(count, cnt)

    answer.add(count)
    user.append((count, name))

print(len(answer))
for i in user:
    print(*i)