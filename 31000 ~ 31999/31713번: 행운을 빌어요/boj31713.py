# 백준 31713번 행운을 빌어요
import sys
from math import ceil
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    A, B = map(int, put().split())

    # 잎을 더 가져와야 하는 경우
    if A * 3 > B:
        print(A * 3 - B)

    # 줄기/잎을 더 가져와야 하는 경우
    else:
        answer = set()
        for leaf_4 in range(B // 4 + 1):
            leaf_3 = ceil((B - leaf_4 * 4) / 3)

            a = leaf_3 + leaf_4 - A
            b = leaf_3 * 3 + leaf_4 * 4 - B

            if a + b >= 0:
                answer.add(a + b)

        print(min(answer))