# 백준 33163번 OIJ (OIJ)
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
chg = {'J': 'O', 'O': 'I', 'I': 'J'}

print(''.join([chg[i] for i in S]))