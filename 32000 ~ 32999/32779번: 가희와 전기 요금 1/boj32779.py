# 백준 32779번 가희와 전기 요금 1
import sys
put = sys.stdin.readline

Q = int(put())

while Q:
    Q -= 1
    a, m = map(int, put().split())
    answer = a * m * 105.6 / (1000 * 60)
    print(int(answer))