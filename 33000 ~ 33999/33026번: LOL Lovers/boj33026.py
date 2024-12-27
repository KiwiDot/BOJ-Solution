# 백준 33026번 LOL Lovers
import sys
put = sys.stdin.readline

n = int(put())
food = put().strip()

for i in range(1, n):
    a, b = food[:i], food[i:]

    if a.count('L') != b.count('L') and a.count('O') != b.count('O'):
        print(i)
        break

else:
    print(-1)