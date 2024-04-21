# 백준 29601번 Железная дорога
import sys
from math import ceil
put = sys.stdin.readline

text = put().strip()
train, num = text[0], int(text[1:])
a = b = c = 0

# 불가능한 좌석 번호
if train == 'C' and num > 36:
    print(-1)

else:
    # 접이식 좌석
    if num > 36:
        a = (54 - num) // 2 + 1

    # 일반 좌석
    else:
        a = ceil(num / 4)
        b = 1

    c = -1 if num % 2 else 1

    print(a, b, c)