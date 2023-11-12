# 백준 30501번 관공... 어찌하여 목만 오셨소...
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    name = put().strip()

    if 'S' in name:
        print(name)
