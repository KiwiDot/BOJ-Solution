# 백준 32386번 KCPC에 등장할 알고리즘 맞히기
import sys
from collections import defaultdict
put = sys.stdin.readline

N = int(put())
tag = defaultdict(int)

while N:
    N -= 1
    data = put().split()

    for i in data[2:]:
        tag[i] += 1

value = list(tag.values())
if value.count(max(value)) == 1:
    print(max(tag, key=tag.get))
else:
    print(-1)