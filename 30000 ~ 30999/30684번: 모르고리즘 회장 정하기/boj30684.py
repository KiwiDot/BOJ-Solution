# 백준 30684번 모르고리즘 회장 정하기
import sys
put = sys.stdin.readline

N = int(put())
S = []

while N:
    N -= 1
    name = put().strip()
    if len(name) == 3:
        S.append(name)

print(sorted(S)[0])