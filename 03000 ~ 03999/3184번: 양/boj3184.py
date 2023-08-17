# 백준 3184번 양
import sys
from collections import deque
put = sys.stdin.readline

R, C = map(int, put().split())
data = [list(put().strip()) for i in range(R)]
answer = {'o': 0, 'v': 0}

for i in range(R):
    for j in range(C):
        if data[i][j] == '#':
            continue

        cnt = {'o': 0, 'v': 0, '.': 0}
        cnt[data[i][j]] += 1
        data[i][j] = '#'

        visit = deque([(i, j)])
        while visit:
            r, c = visit.popleft()
            for ri, ci in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= ri < R and 0 <= ci < C and data[ri][ci] != '#':
                    visit.append((ri, ci))
                    cnt[data[ri][ci]] += 1
                    data[ri][ci] = '#'

        if cnt['o'] > cnt['v']:
            cnt['v'] = 0
        else:
            cnt['o'] = 0

        answer['o'] += cnt['o']
        answer['v'] += cnt['v']

print(answer['o'], answer['v'])