# 백준 14888번 연산자 끼워넣기
import sys
put = sys.stdin.readline


def solution(n, number):
    if n == N:
        answer.add(number)

    else:
        for i in range(4):
            if o[i]:
                o[i] -= 1
                num = int(eval(str(number) + operator[i] + str(A[n])))
                solution(n+1, num)
                o[i] += 1


N = int(put())
A = list(map(int, put().split()))
o = list(map(int, put().split()))
operator = ['+', '-', '*', '/']
answer = set()

solution(1, A[0])

print(max(answer))
print(min(answer))