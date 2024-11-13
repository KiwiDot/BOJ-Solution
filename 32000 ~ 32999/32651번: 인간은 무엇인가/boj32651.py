# 백준 32651번 인간은 무엇인가
import sys
put = sys.stdin.readline

N = int(put())

print("No" if N % 2024 or N > 100_000 else "Yes")