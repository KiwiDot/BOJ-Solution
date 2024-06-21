# 백준 31927번 렬정! 렬정! 렬정!
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
x = 10 ** 6

print(N // 2)
for i in range(N // 2):
    A[i] += x
    A[-i-1] -= x

    print(*A)
    x -= 5000