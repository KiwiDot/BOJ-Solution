# 백준 31246번 모바일 광고 입찰
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
diff = []

while N:
    N -= 1
    A, B = map(int, put().split())
    diff.append(B - A)

diff.sort()
answer = diff[K-1]

print(answer if answer > 0 else 0)