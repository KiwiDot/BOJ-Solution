# 백준 31432번 소수가 아닌 수 3
import sys
put = sys.stdin.readline

N = int(put())
d = sorted([i for i in put().split() if i != '0'])

print("YES")
if not d:
    print("0")
else:
    print(d[-1] * 4)
