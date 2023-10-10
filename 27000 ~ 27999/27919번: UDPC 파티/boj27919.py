# 백준 27919번 UDPC 파티
import sys
from math import ceil
put = sys.stdin.readline

cnt = {'U': 0, 'D': 0, 'P': 0, 'C': 0}
V = put().strip()

for i in V:
    cnt[i] += 1

U = cnt['U'] + cnt['C']
DP = cnt['D'] + cnt['P']

answer = ""
if U > ceil(DP / 2):
    answer += 'U'
if DP:
    answer += 'DP'
print(answer)