# 백준 31518번 Triple Sevens
import sys
put = sys.stdin.readline

n = int(put())
m1 = set(put().split())
m2 = set(put().split())
m3 = set(put().split())

if '7' in m1 & m2 & m3:
    print(777)
else:
    print(0)