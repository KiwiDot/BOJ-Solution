# 백준 30167번 Distinct Digits
import sys
put = sys.stdin.readline

l, r = map(int, put().split())

for x in range(l, r+1):
    if len(str(x)) == len(set(str(x))):
        print(x)
        break

else:
    print(-1)