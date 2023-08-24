# 백준 17615번 볼 모으기
import sys
put = sys.stdin.readline

N = int(put())
ball = put().strip()[::-1]
RB = BR = R = B = 0
rb = br = r = b = 0

for i in ball:
    if i == 'R':
        R = 1
        r += 1
        if B:
            BR += 1
            rb += b
            b = 0

    else:
        B = 1
        b += 1
        if R:
            RB += 1
            br += r
            r = 0

print(min(RB, BR, rb, br))