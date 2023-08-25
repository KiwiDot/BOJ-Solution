# 백준 29546번 Файлы
import sys
put = sys.stdin.readline

n = int(put())
file = [put().strip() for i in range(n)]

m = int(put())
while m:
    m -= 1
    l, r = map(int, put().split())
    print("\n".join(file[l-1:r]))