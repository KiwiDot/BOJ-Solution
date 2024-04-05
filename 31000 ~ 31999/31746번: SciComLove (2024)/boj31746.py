# 백준 31746번 SciComLove (2024)
import sys
put = sys.stdin.readline

text = "SciComLove"
N = int(put())

if N % 2:
    print(text[::-1])
else:
    print(text)