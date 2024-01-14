# 백준 31261번 НАМИСЛИХ СИ ЧИСЛО
import sys
put = sys.stdin.readline

a, b = map(int, put().split())

print(((b + a) * a + a) * a)