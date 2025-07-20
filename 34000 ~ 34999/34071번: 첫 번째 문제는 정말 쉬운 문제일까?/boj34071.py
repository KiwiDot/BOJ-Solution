# 백준 34071번 첫 번째 문제는 정말 쉬운 문제일까?
import sys
put = sys.stdin.readline

N = int(put())
n = [int(put()) for i in range(N)]

if min(n) == n[0]:
    print("ez")
elif max(n) == n[0]:
    print("hard")
else:
    print("?")