# 백준 1138번 한 줄로 서기
import sys
put = sys.stdin.readline

N = int(put())
n = list(map(int, put().split()))
answer = ['-'] * N
idx = [i for i in range(N)]

for i in range(N):
    answer[idx.pop(n[i])] = i + 1

print(*answer)