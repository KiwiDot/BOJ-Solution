# 백준 32777번 가희와 서울 지하철 2호선
import sys
put = sys.stdin.readline

Q = int(put())

while Q:
    Q -= 1
    a, b = map(int, put().split())

    inner = ((b - a + 243) % 243) % 200
    outer = ((a - b + 243) % 243) % 200

    print("Inner" if inner < outer else "Outer", "circle line")