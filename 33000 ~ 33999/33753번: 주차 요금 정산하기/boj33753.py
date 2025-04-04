# 백준 33753번 주차 요금 정산하기
import sys
from math import ceil
put = sys.stdin.readline

A, B, C = map(int, put().split())
T = int(put())

answer = A + ceil(max(T - 30, 0) / B) * C
print(answer)