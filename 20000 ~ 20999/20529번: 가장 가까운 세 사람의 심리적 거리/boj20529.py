# 백준 20529번 가장 가까운 세 사람의 심리적 거리
import sys
from itertools import combinations
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N = int(put())
    student = [set(i) for i in put().split()]

    # 학생이 48명 이상일 경우 반드시 동일한 MBTI를 가진 학생이 3명 이상 존재한다
    if N >= 48:
        print(0)

    else:
        answer = 12
        for i, j, k in combinations([i for i in range(N)], 3):
            A = student[i]
            B = student[j]
            C = student[k]

            diff = 12 - len(A & B) - len(B & C) - len(C & A)
            answer = min(answer, diff)

        print(answer)


