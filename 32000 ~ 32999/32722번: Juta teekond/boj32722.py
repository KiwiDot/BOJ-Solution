# 백준 32722번 Juta teekond
import sys
put = sys.stdin.readline

n = [int(put()) for i in range(3)]

if n[0] in {1, 3} and n[1] in {6, 8} and n[2] in {2, 5}:
    print("JAH")
else:
    print("EI")