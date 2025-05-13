# 백준 33845번 PNUPC에 한 번도 빠지지 않고 출연한 산지니가 새삼 대단하다고 느껴지네
import sys
put = sys.stdin.readline

S = set(put().strip())
T = put().strip()

print(''.join([i for i in T if i not in S]))