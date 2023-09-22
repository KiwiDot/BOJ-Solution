# 백준 29615번 알파빌과 베타빌
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
n = list(map(int, put().split()))
friend = set(map(int, put().split()))

print(len(friend - set(n[:M])))