# 백준 26904번 Tågväxeln
import sys
put = sys.stdin.readline

n, m = sorted(list(map(int, put().split())))
answer = 0
switch = 0

for i in range(1, 1440):
    if i % n == 0 and switch != 0:
        switch ^= 1
        answer += 1

    if i % m == 0 and switch != 1:
        switch ^= 1
        answer += 1

print(answer)