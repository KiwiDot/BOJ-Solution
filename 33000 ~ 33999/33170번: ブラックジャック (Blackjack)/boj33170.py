# 백준 33170번 ブラックジャック (Blackjack)
import sys
put = sys.stdin.readline

A, B, C = [int(put()) for i in range(3)]

print(0 if A + B + C > 21 else 1)