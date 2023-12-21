# 백준 30979번 유치원생 파댕이 돌보기
import sys
put = sys.stdin.readline

T = int(put())
N = int(put())
F = list(map(int, put().split()))

if sum(F) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")