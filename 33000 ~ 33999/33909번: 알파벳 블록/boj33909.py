# 백준 33909번 알파벳 블록
import sys
put = sys.stdin.readline

S, C, O, N = map(int, put().split())

C += O * 2
S += N

answer = min(C//6, S//3)
print(answer)