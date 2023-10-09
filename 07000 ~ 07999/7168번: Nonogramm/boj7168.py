# 백준 7168번 Nonogramm
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = [list(put().strip()) for i in range(N)]

for i in range(N):
    d = ''.join(data[i]).split('.')
    answer = [len(j) for j in d if j != '']
    if answer:
        print(*answer)
    else:
        print(0)

for j in range(M):
    d = ''.join([data[i][j] for i in range(N)]).split('.')
    answer = [len(j) for j in d if j != '']
    if answer:
        print(*answer)
    else:
        print(0)