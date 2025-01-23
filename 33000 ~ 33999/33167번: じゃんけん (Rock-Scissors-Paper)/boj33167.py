# 백준 33167번 じゃんけん (Rock-Scissors-Paper)
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
T = put().strip()
answer = [0, 0]

for s, t in zip(S, T):
    if s == 'R' and t == 'R':
        continue
    elif s == 'S' and t == 'P':
        answer[0] += 1
    elif s == 'R' and t == 'P':
        answer[1] += 1
    elif s == 'S' and t == 'R':
        answer[1] += 1

print(answer[0], answer[1])
