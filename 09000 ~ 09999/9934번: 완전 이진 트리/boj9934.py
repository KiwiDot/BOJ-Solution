# 백준 9934번 완전 이진 트리
import sys
put = sys.stdin.readline


def solution(num, d):
    if len(num) == 1:
        answer[d].append(num[0])
        return

    L = len(num) // 2
    answer[d].append(num[L])

    solution(num[:L], d + 1)
    solution(num[L+1:], d + 1)
    return 0


K = int(put())
n = list(map(int, put().split()))
answer = [[] for i in range(K)]

solution(n, 0)
for i in answer:
    print(*i)