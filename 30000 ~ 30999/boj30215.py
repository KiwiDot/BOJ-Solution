# 백준 30215번 Age Expression
import sys
put = sys.stdin.readline

O, A, K = map(int, put().split())
answer = 0

for a in range(1, 151):
    for k in range(1, 151):
        if O == a * A + k * K:
            answer = 1

print(answer)