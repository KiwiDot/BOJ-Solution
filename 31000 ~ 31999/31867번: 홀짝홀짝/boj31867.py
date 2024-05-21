# 백준 31867번 홀짝홀짝
import sys
put = sys.stdin.readline

N = int(put())
K = put().strip()
odd = sum([1 for i in K if int(i) % 2])
even = N - odd

if odd > even:
    print(1)
elif odd < even:
    print(0)
else:
    print(-1)