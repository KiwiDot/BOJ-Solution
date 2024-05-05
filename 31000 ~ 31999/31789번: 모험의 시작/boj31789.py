# 백준 31789번 모험의 시작
import sys
put = sys.stdin.readline

N = int(put())
X, S = map(int, put().split())
weapon = [list(map(int, put().split())) for i in range(N)]

p = max([i[1] for i in weapon if i[0] <= X] + [0])
print("YES" if p > S else "NO")