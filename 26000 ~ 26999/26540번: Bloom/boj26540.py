# 백준 26540번 Bloom
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    x = int(put())
    bloom = [list(map(int, put().split())) for i in range(x)]
    date = int(put())
    answer = 0

    for i in bloom:
        d = i.pop(-1)
        if d == -1:
            if sum(i) == date:
                answer += 1

        elif sum(i) <= date:
            b = date - sum(i)
            if b % sum(i[d:]) == 0:
                answer += 1

    print(answer)