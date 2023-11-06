# 백줃 30585번 Поп-ит
import sys
put = sys.stdin.readline

h, w = map(int, put().split())
cnt = {'0': 0, '1': 0}

while h:
    h -= 1
    pop_it = put().strip()
    for i in pop_it:
        cnt[i] += 1

print(min(cnt.values()))