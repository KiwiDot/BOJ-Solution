# 백준 33910번 합의 최소
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))[::-1]
answer = 0
minimum = 10 ** 9

for i in A:
    minimum = min(minimum, i)
    answer += minimum

print(answer)