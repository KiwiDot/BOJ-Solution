# 백준 31612번 画数数え (Stroke Count)
import sys
put = sys.stdin.readline
cnt = {'j': 2, 'o': 1, 'i': 2}

N = int(put())
S = put().strip()
answer = sum([cnt[i] for i in S])

print(answer)