# 백준 32141번 카드 게임 (Easy)
import sys
put = sys.stdin.readline

N, H = map(int, put().split())
d = list(map(int, put().split()))
answer = h = 0

for i in d:
    answer += 1
    h += i
    if h >= H:
        print(answer)
        break

else:
    print(-1)