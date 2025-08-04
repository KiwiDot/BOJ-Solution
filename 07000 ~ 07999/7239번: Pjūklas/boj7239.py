# 백준 7239번 Pjūklas
import sys
put = sys.stdin.readline

N = int(put())
answer = sorted(list(map(int, put().split())))

for i in range(1, N - 1, 2):
    answer[i], answer[i+1] = answer[i+1], answer[i]

print(*answer)
