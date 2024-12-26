# 백준 32953번 회상
import sys
from collections import defaultdict
put = sys.stdin.readline

N, M = map(int, put().split())
m = defaultdict(int)

while N:
    N -= 1
    K = int(put())
    Ki = put().split()

    for i in Ki:
        m[i] += 1

answer = 0
for i in m.values():
    if i >= M:
        answer += 1

print(answer)