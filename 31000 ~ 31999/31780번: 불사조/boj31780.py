# 백준 31780번 불사조
import sys
from math import ceil, floor
put = sys.stdin.readline

X, M = map(int, put().split())
answer = X
x = [X]

for i in range(M):
    xi = []
    for j in range(len(x)):
        xi += [ceil(x[j] / 2), floor(x[j] / 2)]

    answer += sum(xi)
    x = xi

print(answer)

# 다른 사람의 코드
# print(X * (M + 1))
