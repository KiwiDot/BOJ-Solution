# 백준 31712번 핑크빈 레이드
import sys
put = sys.stdin.readline

Cu, Du = map(int, put().split())
Cd, Dd = map(int, put().split())
Cp, Dp = map(int, put().split())
H = int(put())

for i in range(1000 * 5000):
    if i % Cu == 0:
        H -= Du
    if i % Cd == 0:
        H -= Dd
    if i % Cp == 0:
        H -= Dp

    if H <= 0:
        print(i)
        break