# 백준 29847번 Character Frequencies
import sys
from collections import defaultdict
put = sys.stdin.readline

N = int(put())
cnt = defaultdict(int)

while N:
    N -= 1
    text = put().strip()
    for i in text:
        if i != ' ':
            cnt[i] += 1

for i in cnt:
    print(i, cnt[i])