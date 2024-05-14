# 백준 31824번 근로장학생
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = sorted([put().split() for i in range(N)])

while M:
    M -= 1
    S = put().strip()
    answer = ""

    for i in range(len(S)):
        for Q, A in data:
            if S[i:i+len(Q)] == Q:
                answer += A

    print(answer if answer else -1)