# 백준 31784번 포닉스의 문단속
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
S = [ord(i) - 65 for i in put().strip()]

for i in range(N):
    s = 26 - S[i]
    if s < 26 and s <= K:
        S[i] = 0
        K -= s

K %= 26
S[-1] = (S[-1] + K) % 26
answer = ''.join([chr(i + 65) for i in S])

print(answer)