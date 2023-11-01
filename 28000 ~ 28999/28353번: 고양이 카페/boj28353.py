# 백준 28353번 고양이 카페
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
w = sorted(list(map(int, put().split())))

answer = 0
while w:
    wi = w.pop(0)

    while w and wi + w[-1] > K:
        w.pop(-1)

    if w:
        wi += w.pop()
        if wi <= K:
            answer += 1

print(answer)