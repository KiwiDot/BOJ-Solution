# 백준 19858번 Золотые слитки
import sys
put = sys.stdin.readline

x1, x2, x3 = map(int, put().split())
x = x1 + x2 + x3
answer = []

if x in [x1 * 2, x2 * 2, x3 * 2]:
    print(0)

else:
    for a, b, c, d in [(x1, x2, x3, 1), (x2, x3, x1, 2), (x3, x1, x2, 3)]:
        bc = abs(b - c)
        if a - bc > 0 and (a - bc) % 2 == 0 and not answer:
            abc = (a - bc) // 2
            answer.append(d)
            answer += [abc + bc, abc]

    if answer:
        print(answer[0])
        print(*answer[1:])
    else:
        print(-1)