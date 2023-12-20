# 백준 30957번 빅데이터 vs 정보보호 vs 인공지능
import sys
put = sys.stdin.readline

N = int(put())
cnt = {'B': 0, 'S': 0, 'A': 0}

data = put().strip()
for i in data:
    cnt[i] += 1

maximum = max(cnt.values())
answer = ''.join([i for i in cnt if cnt[i] == maximum])
print("SCU" if answer == "BSA" else answer)