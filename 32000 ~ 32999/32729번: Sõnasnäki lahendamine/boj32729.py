# 백준 32729번 Sõnasnäki lahendamine
import sys
from collections import Counter
put = sys.stdin.readline

text = put().strip()
cnt = Counter(text)
N = int(put())

while N:
    N -= 1
    t = put().strip()

    if len(t) > len(text) or not set(t).issubset(set(text)):
        continue

    c = Counter(t)
    for i in c:
        if c[i] > cnt[i]:
            break

    else:
        print(t)