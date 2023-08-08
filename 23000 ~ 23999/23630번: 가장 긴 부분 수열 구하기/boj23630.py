# 백준 23630번 가장 긴 부분 수열 구하기
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
n = len(bin(max(A))[2:])

answer = [0] * n
for Ai in A:
    a = bin(Ai)[2:].zfill(n)
    for i in range(n):
        if a[i] == '1':
            answer[i] += 1

print(max(answer))