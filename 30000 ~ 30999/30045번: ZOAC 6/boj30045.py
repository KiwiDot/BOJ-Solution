# 백준 30045번 ZOAC 6
import sys
put = sys.stdin.readline

N = int(put())
answer = 0

while N:
    N -= 1
    S = put().strip()
    answer += '01' in S or 'OI' in S

print(answer)