# 백준 32297번 문자열을 만들어요
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()

print("YES" if "gori" in S else "NO")