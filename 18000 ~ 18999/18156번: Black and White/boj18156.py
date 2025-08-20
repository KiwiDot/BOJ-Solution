# 백준 18156번 Black and White
import sys
put = sys.stdin.readline

n = int(put())
row = [list(put().strip()) for i in range(n)]
col = list(map(list, zip(*row)))
answer = 1

for arr in [row, col]:
    for i in arr:
        s = ''.join(i)
        if s.count('B') != s.count('W') or "BBB" in s or "WWW" in s:
            answer = 0
            break
    else:
        continue
    break

print(answer)