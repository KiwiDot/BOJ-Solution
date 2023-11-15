# 백준 30457번 단체줄넘기
import sys
from collections import Counter
put = sys.stdin.readline

N = int(put())
A = list(map(int, put().split()))

cnt = dict(Counter(A))
answer = 0

for i in cnt:
    answer += min(cnt[i], 2)

print(answer)