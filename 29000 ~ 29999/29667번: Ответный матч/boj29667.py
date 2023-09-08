# 백준 29667번 Ответный матч
import sys
put = sys.stdin.readline

a1, b1 = map(int, put().strip().split(':'))
b2, a2 = map(int, put().strip().split(':'))

if a1 < b2 or a2 > b1:
    print("NO")
else:
    print("YES")