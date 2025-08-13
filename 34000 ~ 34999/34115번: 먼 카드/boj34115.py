# 백준 34115번 먼 카드
import sys
put = sys.stdin.readline

N = int(put())
X = list(map(int, put().split()))
check = [-1] * (N+1)

for i in range(N*2):
    if check[X[i]] == -1:
        check[X[i]] = i
    else:
        check[X[i]] = i - check[X[i]] - 1

print(max(check))