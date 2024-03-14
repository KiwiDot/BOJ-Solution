# 백준 31616번 揃った文字 (Matched Letters)
import sys
put = sys.stdin.readline

N = int(put())
S = set(put().strip())

print("Yes" if len(S) == 1 else "No")