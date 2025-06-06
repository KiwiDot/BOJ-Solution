# 백준 33924번 신묘마루의 요술망치
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
K = int(put())
S = put().strip()

N -= 1
M -= 1

for i in S:
    match i:
        case 'A':
            N = (N + 2) % 4

        case 'B':
            N += -1 if N % 2 else 1
            M ^= 1

        case 'C':
            N = [3, 2, 1, 0][N]
            M ^= 1

        case 'D':
            if M:
                if N == 3:
                    M -= 1
                N = min(N+1, 3)
            else:
                if N == 0:
                    M += 1
                N = max(N-1, 0)

print(N+1, M+1)