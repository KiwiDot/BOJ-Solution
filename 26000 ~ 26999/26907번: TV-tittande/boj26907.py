# 백준 26907번 TV-tittande
import sys
put = sys.stdin.readline

N = int(put())
tv = []
answer = [0] * N

for _ in range(N):
    data = put().split()
    r = data.pop(0)

    cnt = set()
    for i in data:
        t1, t2 = i.split('-')
        h1, m1 = map(int, t1.split(':'))
        h2, m2 = map(int, t2.split(':'))

        for j in range(h1*60+m1, h2*60+m2+1):
            cnt.add(j)

    tv.append(cnt)

idx = 0
for i in range(1440):
    if i in tv[idx]:
        idx = (idx + 1) % N
    else:
        answer[idx] += 1

for i in answer:
    print(i)