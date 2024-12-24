# 백준 32941번 왜 맘대로 예약하냐고
import sys
put = sys.stdin.readline

T, X = map(int, put().split())
N = int(put())

answer = "YES"
while N:
    N -= 1
    K = int(put())
    A = set(map(int, put().split()))

    if X not in A:
        answer = "NO"
        break

print(answer)