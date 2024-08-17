# 백준 30686번 과제 제출하기
import sys
from itertools import permutations
put = sys.stdin.readline

N, M = map(int, put().split())
d = list(map(int, put().split()))
a = [list(map(lambda x: int(x) - 1, put().split()))[1:] for i in range(M)]
answer = set()

# 순열로 모든 경우의 수 탐색
for p in permutations([i for i in range(M)]):
    cnt = day = 0
    knowledge = [0] * N

    # m번 문제
    for m in p:
        # m번 문제를 풀기 위해 필요한 지식
        for i in a[m]:
            if knowledge[i] <= day:
                cnt += 1
                knowledge[i] = day + d[i]
        day += 1

    answer.add(cnt)

print(min(answer))