# 백준 3003번 킹,퀸,룩,비숍,나이트,폰
import sys
put = sys.stdin.readline

chess = list(map(int, put().split()))
perfect = [1, 1, 2, 2, 2, 8]
answer = [perfect[i] - chess[i] for i in range(6)]

print(*answer)
