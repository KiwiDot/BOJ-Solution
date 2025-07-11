# 백준 26884번 Kent-buggen
import sys
from collections import Counter
put = sys.stdin.readline

n = int(put())
names = [put().strip() for i in range(n)]
cnt = dict(Counter(names))

answer = sum(1 for i in cnt.values() if i > 1)

print(answer)
