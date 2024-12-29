# 백준 33046번 Alea Iacta Est
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
C, D = map(int, put().split())

gadong = (A + B) % 4

player = ''.join([str((gadong + i) % 4) for i in range(4)])
player = player.replace('0', '4')

jindong = player[(C + D - 1) % 4]
print(jindong)