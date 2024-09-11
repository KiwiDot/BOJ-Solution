# 백준 32217번 광선 다각형 만들기
import sys
put = sys.stdin.readline

n = int(put())
answer = (n - 1) * 180 - sum(list(map(int, put().split()))) * 2

print(answer)