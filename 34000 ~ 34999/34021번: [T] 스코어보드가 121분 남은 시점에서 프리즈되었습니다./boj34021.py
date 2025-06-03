# 백준 34021번 [T] 스코어보드가 121분 남은 시점에서 프리즈되었습니다.
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N, M, L = map(int, put().split())
    S = [i for i in list(map(int, put().split())) if i > -1] + [M - L]

    X = M - min(S)

    if X == 1:
        answer = f'{X} minute'
    else:
        answer = f'{X} minutes'

    print(f"The scoreboard has been frozen with {answer} remaining.")
