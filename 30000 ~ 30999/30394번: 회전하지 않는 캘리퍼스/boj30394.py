# 백준 30394번 회전하지 않는 캘리퍼스
import sys
put = sys.stdin.readline

N = int(put())
x = set()
y = set()

while N:
    N -= 1
    xi, yi = map(int, put().split())
    x.add(xi)
    y.add(yi)

print(max(y) - min(y))