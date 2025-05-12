# 백준 17264번 I AM IRONMAN
import sys
put = sys.stdin.readline

N, P = map(int, put().split())
W, L, G = map(int, put().split())
win = set()

while P:
    P -= 1
    nickname, result = put().split()
    if result == 'W':
        win.add(nickname)

score = 0
while N:
    N -= 1
    nickname = put().strip()

    if nickname in win:
        score += W
    else:
        score = max(score - L, 0)

    if score >= G:
        print("I AM NOT IRONMAN!!")
        break
else:
    print("I AM IRONMAN!!")
