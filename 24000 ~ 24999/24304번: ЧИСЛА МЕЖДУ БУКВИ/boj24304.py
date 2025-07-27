# 백준 24304번 ЧИСЛА МЕЖДУ БУКВИ
import sys
put = sys.stdin.readline

N = int(put())
s = ''.join(i if i.isdigit() else ' ' for i in put().strip()).split()

if s:
    for i in s:
        print(N * int(i))
else:
    print('N/A')