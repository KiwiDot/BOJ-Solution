# 백준 4673번 셀프 넘버
import sys
put = sys.stdin.readline

number = [1] * 10 ** 5

for i in range(1, 10001):
    if number[i]:
        print(i)

    n = i + sum(list(map(int, str(i))))
    number[n] = 0