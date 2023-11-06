# 백준 30454번 얼룩말을 찾아라!
import sys
put = sys.stdin.readline

N, L = map(int, put().split())
zebra = {}

while N:
    N -= 1
    z = put().strip().split('0')
    cnt = sum([i != '' for i in z])

    if cnt in zebra:
        zebra[cnt] += 1
    else:
        zebra[cnt] = 1

answer = max(zebra)
print(answer, zebra[answer])