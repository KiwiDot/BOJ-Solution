# 백준 17374번 비트베리
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    P, Q, A, B, C, D = map(int, put().split())

    # 베리 -> 코인
    R = Q // C * D  # R은 코인

    # 비트 -> 코인
    R += P // A * B
    P %= A

    answer = {0}
    start = 0
    end = R // B

    while start <= end:
        n = (start + end) // 2
        p = P + A * n
        r = R - B * n

        answer.add(min(p, r))

        if p > r:
            end = n - 1
        else:
            start = n + 1

    print(max(answer))