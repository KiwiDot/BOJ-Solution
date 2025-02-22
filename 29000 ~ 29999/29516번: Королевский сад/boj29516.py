# 백준 29516번 Королевский сад
import sys
put = sys.stdin.readline

a, b = map(int, put().split())
data = [put().strip() for _ in range(a)]
answer = "No"

# row
tree = [data[i] for i in range(a)]
cnt = 0
for i in tree:
    if len(set(i)) > 1:
        cnt += 1
if cnt <= 1:
    answer = "Yes"

# col
tree = [''.join([data[j][i] for j in range(a)]) for i in range(b)]
cnt = 0
for i in tree:
    if len(set(i)) > 1:
        cnt += 1
if cnt <= 1:
    answer = "Yes"

print(answer)