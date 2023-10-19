# 백준 30266번 Hurricane Warning
import sys
put = sys.stdin.readline

K = int(put())

for x in range(1, K+1):
    n = int(put())
    check = set(put().strip())
    answer = 0

    while n:
        n -= 1
        data = set(put().strip())

        answer += 1 if data & check else 0

    print("Data Set {}:".format(x))
    print(answer)
    print()
