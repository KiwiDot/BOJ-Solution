# 백준 29736번 브실이와 친구가 되고 싶어 🤸‍♀️
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
K, X = map(int, put().split())

ab = set(i for i in range(A, B+1))
k = set(i for i in range(max(1, K-X), K+X+1))

if ab & k:
    print(len(ab & k))
else:
    print("IMPOSSIBLE")