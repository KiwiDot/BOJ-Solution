# 백준 30224번 Lucky 7
import sys
put = sys.stdin.readline

n = put().strip()
print(1 + int('7' in n) * 2 - bool(int(n) % 7))