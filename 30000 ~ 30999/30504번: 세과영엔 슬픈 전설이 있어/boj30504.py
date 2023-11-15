# 백준 30504번 세과영엔 슬픈 전설이 있어
import sys
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))
B = sorted(list(map(int, put().split())))

a = sorted([[A[i], i] for i in range(N)])
money = [a[i] + [B[i]] for i in range(N)]

answer = [i[2] for i in sorted(money, key=lambda x:x[1])]

for i in range(N):
    if answer[i] < A[i]:
        print(-1)
        break
else:
    print(*answer)