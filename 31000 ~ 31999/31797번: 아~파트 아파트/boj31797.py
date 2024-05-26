# 백준 31797번 아~파트 아파트
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
hand = []

for i in range(M):
    H1, H2 = map(int, put().split())
    hand += [(H1, i+1), (H2, i+1)]

hand.sort()
idx = (N - 1) % (M * 2)
print(hand[idx][1])