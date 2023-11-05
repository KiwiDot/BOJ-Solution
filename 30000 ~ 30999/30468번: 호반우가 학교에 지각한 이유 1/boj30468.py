# 백준 30468번 호반우가 학교에 지각한 이유 1
import sys
put = sys.stdin.readline

STR, DEX, INT, LUK, N = map(int, put().split())

answer = max(N * 4 - (STR + DEX + INT + LUK), 0)
print(answer)