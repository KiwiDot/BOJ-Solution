# 백준 30553번 Guess Who
import sys
put = sys.stdin.readline

N, M, Q = map(int, put().split())
string = [put().strip() for i in range(N)]
check = ['?'] * M

for i in range(Q):
    A, answer = put().split()
    check[int(A)-1] = answer

answer = []
for i in range(N):
    for j in range(M):
        if check[j] != '?' and check[j] != string[i][j]:
            break
    else:
        answer.append(i+1)

if len(answer) == 1:
    print("unique")
    print(answer[0])
else:
    print("ambiguous")
    print(len(answer))