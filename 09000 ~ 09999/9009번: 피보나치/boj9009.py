# 백준 9009번 피보나치
import sys
put = sys.stdin.readline

T = int(put())
fibo = [1, 1, 2, 3, 5]

while fibo[-1] < 10 ** 9:
    fibo.append(fibo[-1] + fibo[-2])
fibo = fibo[::-1]

while T:
    T -= 1
    n = int(put())
    answer = []

    for i in fibo:
        if i <= n:
            n -= i
            answer.append(i)

    print(*answer[::-1])