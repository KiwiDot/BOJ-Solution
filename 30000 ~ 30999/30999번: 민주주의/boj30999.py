# 백준 30999번 민주주의
import sys
put = sys.stdin.readline

N, M = map(int, put().split())

answer = 0
while N:
    N -= 1
    data = put().strip()

    O = data.count('O')
    X = M - O
    answer += O > X

print(answer)