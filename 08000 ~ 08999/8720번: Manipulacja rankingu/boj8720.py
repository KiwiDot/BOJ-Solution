# 백준 8720번 Manipulacja rankingu
import sys
put = sys.stdin.readline

n, m = map(int, put().split())

score = [list(map(int, put().split())) for i in range(n)]
check = [0] * n

for i in range(m):
    if score[0][i] == 100:
        for j in range(n):
            if score[j][i] == 100:
                check[j] += 1

# 조작을 하면 무조건 1위는 가능
ranking = 1
answer = check.count(max(check))

print(ranking, answer)