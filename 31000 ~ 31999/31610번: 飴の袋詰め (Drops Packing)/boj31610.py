# 백준 31610번 飴の袋詰め (Drops Packing)
import sys
put = sys.stdin.readline

A, B, C = [int(put()) for i in range(3)]

print(A * B + C)