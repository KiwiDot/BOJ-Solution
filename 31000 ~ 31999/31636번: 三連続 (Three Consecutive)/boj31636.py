# 백준 31636번 三連続 (Three Consecutive)
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()

print("Yes" if "ooo" in S else "No")