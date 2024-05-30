# 백준 31881번 K512에 바이러스 퍼뜨리기
import sys
put = sys.stdin.readline

N, Q = map(int, put().split())
virus = [0] * N
answer = N

while Q:
    Q -= 1
    query = list(map(int, put().split()))

    match query[0]:
        case 1:
            x = query[1] - 1
            if not virus[x]:
                answer -= 1
                virus[x] = 1

        case 2:
            x = query[1] - 1
            if virus[x]:
                answer += 1
                virus[x] = 0

        case 3:
            print(answer)