# 백준 7181번 Mõttemeister
import sys
put = sys.stdin.readline

pw = put().strip()
N = int(put())
cnt = dict([(i, pw.count(str(i))) for i in range(10)])

while N:
    N -= 1
    s = put().strip()

    A = sum([min(cnt[i], s.count(str(i))) for i in range(10)])
    B = sum([pw[i] == s[i] for i in range(4)])

    print(A, B)