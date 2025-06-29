# 백준 33172번 周期文字列 (Cycle String)
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()

for i in range(1, N // 2 + 1):
    if not N % i:
        if S == S[:i] * (N // i):
            print("Yes")
            break
else:
    print("No")
