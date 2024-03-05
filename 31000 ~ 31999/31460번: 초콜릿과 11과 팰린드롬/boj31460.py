# 백준 31460번 초콜릿과 11과 팰린드롬
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())
    n = N // 2

    # 11의 배수 = 홀수자리 숫자의 합 - 짝수자리 숫자의 합
    if N % 4 == 1:
        answer = int('1' * n + '0' + '1' * n)
    elif N % 4 == 3:
        answer = int('1' * n + '2' + '1' * n)
    else:
        answer = int('1' * N)

    print(answer)