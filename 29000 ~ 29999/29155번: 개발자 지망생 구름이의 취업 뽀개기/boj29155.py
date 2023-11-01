# 백준 29155번 개발자 지망생 구름이의 취업 뽀개기
import sys
put = sys.stdin.readline

N = int(put())
p = list(map(int, put().split()))
solve = [[] for i in range(5)]

while N:
    N -= 1
    k, t = map(int, put().split())
    solve[k-1].append(t)

for i in solve:
    i.sort()

answer = -60
for i in range(5):
    answer += sum(solve[i][:p[i]])
    answer += 60
    if p[i] > 1:
        answer += solve[i][p[i]-1] - solve[i][0]
print(answer)