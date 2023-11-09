# 백준 29602번 Расписание
import sys
put = sys.stdin.readline

N = int(put())
t = list(map(int, put().split()))
t = [[t[i], i] for i in range(N)]

t.sort()
t = [t[i] + [i+1] for i in range(N)]

t.sort(key=lambda x: x[1])
answer = [i[-1] for i in t]
print(*answer)