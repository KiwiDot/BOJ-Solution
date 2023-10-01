# 백준 30281번 Saldainiai
import sys
put = sys.stdin.readline

N = int(put())
a = []

# 현재 일부 입력 데이터의 n개의 정수가 줄바꿈으로 구분되어 있음
while len(a) < N:
    a += list(map(int, put().split()))

odd = [i for i in a if i % 2]
answer = sum(a)

if answer % 2:
    answer -= min(odd)
print(answer // 2)