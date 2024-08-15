# 백준 30425번 Re-verse
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
idx = {0}

# 시작 부분과 끝 부분이 최대로 겹치는 부분 찾기
for i in range(N-1):
    if S[:i+1] == S[N-i-1:]:
        idx.add(i+1)
s = (S + S[max(idx):] * N)[:2*N-1]

# 노래를 시작할 수 있는 최대 횟수 찾기
answer = 0
for i in range(len(s)-N+1):
    if S == s[i:i+N]:
        answer += 1

print(answer)