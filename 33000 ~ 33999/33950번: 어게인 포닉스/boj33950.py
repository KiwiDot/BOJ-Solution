# 백준 33950번 어게인 포닉스
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    S = put().strip()
    print(S.replace('PO', 'PHO'))