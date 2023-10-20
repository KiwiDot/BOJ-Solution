# 백준 29683번 Рождественская лотерея
import sys
put = sys.stdin.readline

n, A = map(int, put().split())
a = list(map(int, put().split()))

answer = sum([i // A for i in a])
print(answer)