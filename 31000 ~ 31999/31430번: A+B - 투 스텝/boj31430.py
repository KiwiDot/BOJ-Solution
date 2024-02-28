# 백준 31430번 A+B - 투 스텝
import sys
put = sys.stdin.readline

T = int(put())

# 갑의 입력
if T == 1:
    A, B = map(int, put().split())
    n = A + B
    answer = ""

    while n:
        n, r = divmod(n, 26)
        answer += chr(r + 97)

    answer = answer[::-1].rjust(13, "a")
    print(answer)

# 을의 입력
else:
    n = put().strip()[::-1]
    answer = 0

    for i in range(13):
        answer += (ord(n[i]) - 97) * 26 ** i

    print(answer)