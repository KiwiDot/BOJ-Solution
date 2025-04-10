# 백준 33779번 Back and Forth
import sys
put = sys.stdin.readline

s = put().strip()

print("beep" if s == s[::-1] else "boop")