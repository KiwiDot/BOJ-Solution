# 백준 15824번 너 봄에는 캡사이신이 맛있단다
import sys
put = sys.stdin.readline

N = int(put())
menu = sorted(list(map(int, put().split())))
r = 10 ** 9 + 7
answer = 0

n2 = [1]
for i in range(1, N+1):
    n2.append((n2[-1] * 2) % r)

for i in range(N):
    n = (n2[i] - n2[N-i-1] + r) % r
    answer = (answer + n * menu[i]) % r

print(answer)



