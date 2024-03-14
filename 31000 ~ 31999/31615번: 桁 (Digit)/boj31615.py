# 백준 31615번 桁 (Digit)
import sys
put = sys.stdin.readline

A, B = [int(put()) for i in range(2)]
print(len(str(A + B)))