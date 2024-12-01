# 백준 32775번 가희와 4시간의 벽 1
import sys
put = sys.stdin.readline

Sab = int(put())
Fab = int(put())

print("high speed rail" if Sab <= Fab else "flight")