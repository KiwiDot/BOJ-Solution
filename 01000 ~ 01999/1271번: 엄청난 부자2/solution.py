# 백준 1271번 엄청난 부자2
import sys
put = sys.stdin.readline

n, m = map(int, put().split())

print(n // m)
print(n % m)
