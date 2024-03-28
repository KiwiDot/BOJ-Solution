# 백준 22233번 가희와 키워드
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
keyword = {put().strip() for i in range(N)}

while M:
    M -= 1
    used = set(put().strip().split(','))
    keyword -= used

    print(len(keyword))