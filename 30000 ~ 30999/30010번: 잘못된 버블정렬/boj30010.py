# 백준 30010번 잘못된 버블정렬
import sys
put = sys.stdin.readline

N = int(put())
A = [N] + list(range(1, N))

print(*A)