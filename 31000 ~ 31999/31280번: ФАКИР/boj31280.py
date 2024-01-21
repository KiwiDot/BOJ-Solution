# 백준 31280번 ФАКИР
import sys
put = sys.stdin.readline

abcd = sorted(list(map(int, put().split())))

print(sum(abcd[1:]) + 1)