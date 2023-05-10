# 백준 1003번 피보나치 함수
import sys
put = sys.stdin.readline

fibo = {0: 0, 1: 1, 2: 1}

# 주어진 피보나치 함수를 메모이제이션 형태로 바꾼다
def fibonacci(n):
    if n not in fibo:
        fibo[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibo[n]


T = int(put())

while T:
    T -= 1
    N = int(put())
    fibonacci(N)
    if N == 0:
        print(1, 0)
    else:
        print(fibo[N-1], fibo[N])
