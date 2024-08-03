# 백준 19539번 사과나무
import sys
put = sys.stdin.readline

N = int(put())
h = list(map(int, put().split()))

cnt = {1: 0, 2: 0}
for i in h:
    cnt[2] += i // 2
    cnt[1] += i % 2

if cnt[2] > cnt[1]:
    n = (cnt[2] - cnt[1]) // 3
    cnt[2] -= n
    cnt[1] += n * 2

print("YES" if cnt[1] == cnt[2] else "NO")