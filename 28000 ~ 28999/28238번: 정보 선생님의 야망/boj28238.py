# 백준 28238번 정보 선생님의 야망
import sys
put = sys.stdin.readline

n = int(put())
week = [set() for i in range(5)]

for i in range(n):
    a = list(map(int, put().split()))

    for j in range(5):
        if a[j]:
            week[j].add(i)

cnt = 0
ij = [0, 1]
for i in range(4):
    for j in range(i+1, 5):
        cnt_ij = len(week[i] & week[j])

        if cnt_ij > cnt:
            cnt = cnt_ij
            ij = [i, j]

i, j = ij
answer = [0] * 5
answer[i] = 1
answer[j] = 1

print(cnt)
print(*answer)