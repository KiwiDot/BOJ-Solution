# 백준 30068번 Stovėjimo aikštelė
import sys
put = sys.stdin.readline

M = int(put())
record = {}

while M:
    M -= 1
    T, N = map(int, put().split())

    if N in record:
        print(N, T - record[N])
        record.pop(N)

    else:
        record[N] = T