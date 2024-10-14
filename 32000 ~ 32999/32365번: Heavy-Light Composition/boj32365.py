# 백준 32365번 Heavy-Light Composition
import sys
from collections import Counter
put = sys.stdin.readline

T, N = map(int, put().split())

while T:
    T -= 1
    s = put().strip()
    cnt = Counter(s)

    for i in range(N-1):
        if (cnt[s[i]] > 1) == (cnt[s[i+1]] > 1):
            print('F')
            break

    else:
        print('T')