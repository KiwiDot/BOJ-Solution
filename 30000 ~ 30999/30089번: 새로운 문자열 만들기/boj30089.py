# 백준 30089번 새로운 문자열 만들기
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    S = put().strip()

    for i in range(len(S)+1):
        if S[i:] == S[i:][::-1]:
            X = S[:i]
            print(S + X[::-1])
            break