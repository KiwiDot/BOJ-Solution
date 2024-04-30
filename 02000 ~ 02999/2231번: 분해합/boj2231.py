# 백준 2231번 분해합
import sys
put = sys.stdin.readline

N = int(put())
answer = 0

for i in range(10 ** 6 + 1):
    if i + sum(list(map(int, str(i)))) == N:
        print(i)
        break
else:
    print(0)