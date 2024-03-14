# 백준 31611번 火曜日 (Tuesday)
import sys
put = sys.stdin.readline

X = int(put())
print(1 if X % 7 == 2 else 0)