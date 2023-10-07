# 백준 30310번 Finding Forks
import sys
put = sys.stdin.readline

n = int(put())
a = sorted(list(map(int, put().split())))

print(a[0] + a[1])