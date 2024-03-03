# 백준 31450번 Everyone is a winner
import sys
put = sys.stdin.readline

M, K = map(int, put().split())

print("No" if M % K else "Yes")