# 백준 33213번 Fermatovi Fakini
import sys
put = sys.stdin.readline

N = int(put())
num = list(map(int, put().split()))
n = [int(i) % 2 for i in num]

odd = n.count(1)
even = N - odd

if even > odd:
    ans = {i for i in range(2, 500, 2)}
    print(min(ans - set(num)))

else:
    ans = {i for i in range(1, 500, 2)}
    print(min(ans - set(num)))