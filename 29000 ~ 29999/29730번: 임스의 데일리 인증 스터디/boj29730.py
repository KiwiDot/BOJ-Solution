# 백준 29730번 임스의 데일리 인증 스터디
import sys
put = sys.stdin.readline

N = int(put())
link = []
study = []

while N:
    N -= 1
    n = put().strip()

    if n.startswith("boj.kr/"):
        link.append(n)
    else:
        study.append(n)


study.sort(key=lambda x: [len(x), x])
link.sort(key=lambda x: int(x[7:]))

answer = study + link
for i in answer:
    print(i)