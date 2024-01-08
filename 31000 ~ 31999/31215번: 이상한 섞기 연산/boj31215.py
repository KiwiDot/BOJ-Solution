# 백준 31215번 이상한 섞기 연산
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    n = int(put())
    # i = 1일 때, B1과 B1이 교환, 1은 B1에 존재한다
    # i = 2일 때, B2와 B2가 교환, 1은 B1에 존재한다
    # i = 3일 때, B3와 B1이 교환, 1은 B3에 존재한다
    # 이후부터는 3은 2의 거듭제곱수가 아니기 때문에, B3는 교환이 일어날 일이 없다
    # 따라서 i >= 3인 상황에서는 1은 항상 B3에만 존재한다

    print(1 if n <= 2 else 3)
