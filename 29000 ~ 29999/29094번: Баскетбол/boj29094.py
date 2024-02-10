# 백준 29094번 Баскетбол
import sys
put = sys.stdin.readline

n = int(put())
s = dict([(put().strip(), 0) for i in range(n)])
A = B = 0

m = int(put())
while m:
    m -= 1
    data = put().split()
    a, b = map(int, data[0].split(':'))
    t = data[1]

    s[t] += a - A + b - B
    A, B = a, b

answer = max(s, key=s.get)
print(answer, s[answer])