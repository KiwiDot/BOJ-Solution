# 백준 31833번 온데간데없을뿐더러
import sys
put = sys.stdin.readline

N = int(put())
A = int(''.join(put().split()))
B = int(''.join(put().split()))

print(min(A, B))