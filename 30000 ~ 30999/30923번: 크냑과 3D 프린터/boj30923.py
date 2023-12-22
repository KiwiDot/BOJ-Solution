# 백준 30923번 크냑과 3D 프린터
import sys
put = sys.stdin.readline

N = int(put())
h = list(map(int, put().split()))

diff = [abs(h[i+1] - h[i]) for i in range(N-1)]

answer = N * 2 + sum(diff) + sum(h) * 2 + h[0] + h[-1]
print(answer)