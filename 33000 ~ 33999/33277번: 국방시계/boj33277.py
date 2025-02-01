# 백준 33277번 국방시계
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
D = M * 24 * 60 // N

h, m = divmod(D, 60)
print(f"{str(h).zfill(2)}:{str(m).zfill(2)}")