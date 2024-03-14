# 백준 31608번 ハミング距離 (Hamming Distance)
import sys
put = sys.stdin.readline

N = int(put())
S, T = [put().strip() for i in range(2)]

answer = sum([int(S[i] != T[i]) for i in range(N)])
print(answer)