# 백준 31994번 강당 대관
import sys
put = sys.stdin.readline

data = [put().split() for i in range(7)]
answer = max(data, key=lambda x: int(x[1]))[0]

print(answer)