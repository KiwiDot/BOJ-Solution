# 백준 31654번 Adding Trouble
import sys
put = sys.stdin.readline

A, B, C = map(int, put().split())
print("correct!" if A + B == C else "wrong!")