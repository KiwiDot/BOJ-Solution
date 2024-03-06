# 백준 31066번 비 오는 날
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    N, M, K = map(int, put().split())
    a, b, c, d = N, M, 0, 0

    if M == K == 1 and N > 1:
        print(-1)

    else:
        answer = 0
        while c != N:
            answer += 1

            # 창의인재관 -> 융합인재관
            if b:
                move = min(a, b * K)
                a -= move
                c += move
                b, d = 0, b

            # 융합인재관 -> 창의인재관
            else:
                move = 1
                a += move
                c -= move
                b, d = d, 0

        print(answer)