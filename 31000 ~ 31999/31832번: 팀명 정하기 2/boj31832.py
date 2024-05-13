# 백준 31832번 팀명 정하기 2
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    S = put().strip()

    # 첫 번째 조건
    cnt_upper = cnt_lower = 0
    for i in S:
        if i.isupper():
            cnt_upper += 1
        elif i.islower():
            cnt_lower += 1

    if cnt_upper > cnt_lower:
        continue

    # 두 번째 조건
    if len(S) > 10:
        continue

    # 세 번째 조건
    if S.isdigit():
        continue

    print(S)