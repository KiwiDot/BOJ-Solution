# 백준 30402번 감마선을 맞은 컴퓨터
import sys
put = sys.stdin.readline

data = set()

for i in range(15):
    pixel = set(put().split())
    data |= pixel

answer = {'w': 'chunbae',
          'b': 'nabi',
          'g': 'yeongcheol'}

color = list(data - {'r', 'o', 'y', 'p'})[0]
print(answer[color])