# 백준 25859번 Sort by Frequency
import sys
from collections import Counter
put = sys.stdin.readline

s = put().strip()
cnt = dict(Counter(s))
alpha = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

answer = ''.join(i * j for i, j in alpha)
print(answer)
