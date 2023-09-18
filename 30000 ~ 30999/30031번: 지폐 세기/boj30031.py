# 백준 30031번 지폐 세기
import sys
put = sys.stdin.readline

N = int(put())
cnt = {136: 0, 142: 0, 148: 0, 154: 0}

while N:
    N -= 1
    w, h = map(int, put().split())
    cnt[w] += 1

answer = cnt[136] * 1000 + cnt[142] * 5000 + cnt[148] * 10000 + cnt[154] * 50000
print(answer)