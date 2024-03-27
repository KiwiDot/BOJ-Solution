# 백준 29308번 Закат
import sys
put = sys.stdin.readline

n = int(put())
Russia = []

while n:
    n -= 1
    money, name, country = put().split()
    if country == "Russia":
        Russia.append([int(money), name])

answer = max(Russia, key=lambda x: x[0])[1]
print(answer)