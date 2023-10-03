# 백준 30067번 Paslėpta suma
import sys
put = sys.stdin.readline

num = [int(put()) for i in range(10)]
check = sum(num)

for i in num:
    if i * 2 == check:
        print(i)
        break