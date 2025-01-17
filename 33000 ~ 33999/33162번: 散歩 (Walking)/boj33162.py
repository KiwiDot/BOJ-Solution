# 백준 33162번 散歩 (Walking)
import sys
put = sys.stdin.readline

X = int(put())

if X % 2:
    print(X // 2 + 3)
else:
    print(X // 2)