# 백준 29790번 임스의 메이플컵
import sys
put = sys.stdin.readline

N, U, L = map(int, put().split())
answer = {0: 'Bad', 1: 'Bad', 2: 'Good', 3: 'Very Good'}

print(answer[int(N >= 1000) * 2 + int(U >= 8000 or L >= 260)])