# 백준 32860번 수수수수퍼노바
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
if M <= 26:
    m = chr(M - 1 + 65)
else:
    M -= 27
    m1, m2 = divmod(M, 26)
    m = chr(m1 + 97) + chr(m2 + 97)

print(f"SN {N}{m}")