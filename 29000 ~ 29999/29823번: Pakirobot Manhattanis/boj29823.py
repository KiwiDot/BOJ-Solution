# 백준 29823번 Pakirobot Manhattanis
import sys
put = sys.stdin.readline

N = int(put())
d = put().strip()
cnt = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

for i in d:
    cnt[i] += 1

print(abs(cnt['N'] - cnt['S']) + abs(cnt['E'] - cnt['W']))