# 백준 31776번 예비 소집 결과 보고서
import sys
put = sys.stdin.readline

N = int(put())
answer = 0

while N:
    N -= 1
    T = list(map(int, put().replace("-1", "1000").split()))

    if T == sorted(T) and T[0] < 1000:
        answer += 1

print(answer)