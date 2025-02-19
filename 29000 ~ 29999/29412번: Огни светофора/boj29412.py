# 백준 29412번 Огни светофора
import sys
put = sys.stdin.readline

g, gb, y, r, ry = map(int, put().split())
T = int(put())
cnt = {'r': 0, 'y': 0, 'g': 0, 'gb': 0, 'ry': 0}

light = ['g'] * g + ['gb'] * gb + ['y'] * y + ['r'] * r + ['ry'] * ry

for i in range(T):
    cnt[light[i % len(light)]] += 1

cnt['r'] += cnt['ry']
cnt['y'] += cnt['ry']
cnt['g'] += cnt['gb'] // 2


print(cnt['r'], cnt['y'], cnt['g'])