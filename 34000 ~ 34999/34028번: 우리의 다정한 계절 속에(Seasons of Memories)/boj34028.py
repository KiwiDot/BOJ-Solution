# 백준 34028번 우리의 다정한 계절 속에(Seasons of Memories)
import sys
put = sys.stdin.readline

A, B, C = map(int, put().split())

answer = (A - 2015) * 4 + B // 3 + 1
print(answer)


