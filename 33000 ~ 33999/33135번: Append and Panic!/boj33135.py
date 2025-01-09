# 백준 33135번 Append and Panic!
import sys
put = sys.stdin.readline

S = put().strip()

print(len(S) - len(set(S)))