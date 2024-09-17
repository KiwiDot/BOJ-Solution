# 백준 32314번 Christmas Tree Adapter
import sys
put = sys.stdin.readline

a = int(put())
w, v = map(int, put().split())

print(1 if w / v >= a else 0)