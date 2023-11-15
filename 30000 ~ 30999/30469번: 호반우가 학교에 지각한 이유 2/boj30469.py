# 백준 30469번 호반우가 학교에 지각한 이유 2
import sys
put = sys.stdin.readline

A, B, N = map(int, put().split())
A, B = str(A), str(B)
prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

check = []
for i in ['1', '3', '7']:
    for j in ['1', '3', '7']:
        if i != j:
            ij = ((i + j) * 100)[:N - 4]
            check.append(A + ij + B)
            break

answer = -1
for i in check:
    for j in range(N-1):
        a = i[j:j+2]
        if int(a) not in prime:
            break
    else:
        answer = i
print(answer)