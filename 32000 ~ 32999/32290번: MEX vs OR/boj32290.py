# 백준 32290번 MEX vs OR
import sys
put = sys.stdin.readline

l, r, x = map(int, put().split())
mex = set()

for i in range(l, r+1):
    mex.add(i | x)

answer = {i for i in range(max(mex) + 2)}

print(min(answer - mex))