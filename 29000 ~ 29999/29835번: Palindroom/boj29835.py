# 백준 29835번 Palindroom
import sys
put = sys.stdin.readline

N = int(put())
S = list(put().strip())

answer = 0
for i in range(N//2):
    if S[i] != S[-i - 1]:
        answer += 1
        if S[i] < S[-i-1]:
            S[-i-1] = S[i]
        else:
            S[i] = S[-i-1]

print(answer)
print(''.join(S))
